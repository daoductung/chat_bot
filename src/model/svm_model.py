from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from src.transformer.feature_transformer import FeatureTransformer
from sklearn.linear_model import SGDClassifier


class SVMModel(object):
    def __init__(self):
        self.clf = self._init_pipeline()

    @staticmethod
    def _init_pipeline():
        pipe_line = Pipeline([
            ("transformer", FeatureTransformer()),
            ("vect", CountVectorizer(ngram_range=(0, 1), token_pattern=r'\w{2,}', analyzer='word')),
            ("tfidf", TfidfTransformer()),
            ("clf-svm",
             SGDClassifier(loss='log', penalty='l2', alpha=1e-5, n_iter=5, random_state=None, early_stopping=True))
        ])

        return pipe_line
