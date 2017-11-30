import nltk
from nltk.stem.porter import *


def tokenizeText(text):
    tokens = nltk.word_tokenize(text)
    stemmer = PorterStemmer()
    singles = [stemmer.stem(tokes) for tokes in tokens]
    return singles

