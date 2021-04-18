import pathlib
from glob import glob
import pickle

from sklearn.pipeline import Pipeline


def load_models(directory):
    models = list()
    dir = pathlib.Path(directory)
    for file in glob(dir + '*.pkl'):
        with open(file, 'rb') as f:
            pipeline = pickle.load(f)
            if type(pipeline) == Pipeline:
                models.append(pipeline)
            else:
                print(f'{file} could not be loaded as a model as it is not a sklearn.pipeline.Pipeline type.')


int_to_label_dict = {
    '0': 'negative',
    '1': 'neutral',
    '2': 'positive'
}