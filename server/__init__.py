from flask import Flask, request
import flask_swagger
from server.model_utils import load_models, int_to_label_dict

app = Flask('Text_Classification_Server')
flask_swagger.swagger(app)

models = load_models()


@app.route('/list_models', methods=['GET'])
def list_models():
    formatted_models = [{'id': i, 'model': model.__repr__()} for i, model in enumerate(models)]
    return formatted_models


@app.route('/predict/<id>', methods=['POST'])
def predict(id):
    assert request.method == 'POST', 'Only POST-call allowed at this endpoint'
    text = request.body['text']
    text = text if type(text) == list else [text]
    values = models[id].predict(text)
    labels = [int_to_label_dict[value] for value in values]
    return labels


# class CustomFlaskApp(object):
#
#     def __init__(self):
#         self.app = Flask(__name__)
#         custom_errors = {
#             'JsonInvalidError': {
#                 'status': 500,
#                 'message': 'JSON format not valid'
#             },
#             'JsonRequiredError': {
#                 'status': 400,
#                 'message': 'JSON input required'
#             }
#         }
#         self.api = swagger.docs(Api(self.app, errors=custom_errors), apiVersion=API_VERSION_NUMBER)
#
#         self.api.add_resource(DummyEndpoint, '/dummy', endpoint='dummy')
#         self.api.add_resource(HelloEndpoint, '/hello', endpoint='hello')
#
#     def run(self, *args, **kwargs):
#         self.app.config['PROPAGATE_EXCEPTIONS'] = False
#         self.app.run(*args, **kwargs)
#
#
# def run_app(*args, **kwargs):
#     app = CustomFlaskApp()
#     app.run(*args, **kwargs)
#
#
# if __name__ == '__main__':
#     run_app(debug=True)