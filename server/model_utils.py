import pathlib
from glob import glob
import pickle
from sklearn.pipeline import Pipeline
from spacy.lang.en import English
from spacy.lang.en.stop_words import STOP_WORDS
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

# nlp = English()
#
#
# def featurize_text(text):
#     text = nlp(text)
#     filtered_text = list()
#     for word in text:
#         if (word.is_stop == False) and (word.is_punct == False):
#             filtered_text.append(word.lemma)
#     return filtered_text


def load_models(directory):
    models = list()
    print('.' + directory + '*.pkl')
    print(glob('.' + directory + '*.pkl'))
    for file in glob('.' + directory + '*.pkl'):
        with open(file, 'rb') as f:
            pipeline = pickle.load(f)
            if type(pipeline) == Pipeline:
                models.append(pipeline)
            else:
                print(f'{file} could not be loaded as a model as it is not a sklearn.pipeline.Pipeline type.')
    return models

int_to_label_dict = {
    0: 'negative',
    1: 'neutral',
    2: 'positive'
}