from bayes import *
from whitelist import *
import probabilities
from preprocess import *

class Predict:
    def __init__(self,training_csv: str, filter_stop_words=True, stem_words=True) -> None:
        self.word_to_category_probabilities, self.category_probabilities, self.default_probability = probabilities.get_probabilities(training_csv,filter_stop_words,stem_words)
        self.filter_stop_words = filter_stop_words
        self.stem_words = stem_words
        self.whitelist_dictionary = probabilities.create_whitelist_dictionary(self.word_to_category_probabilities)

    def bayes(self,headline: str):
        return bayes(preprocess(headline,self.filter_stop_words,self.stem_words),self.word_to_category_probabilities,self.category_probabilities,self.default_probability)

    def whitelist(self,headline: str):
        return whitelist(headline,self.whitelist_dictionary,self.filter_stop_words,self.stem_words)
