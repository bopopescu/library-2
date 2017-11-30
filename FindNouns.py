import nltk
import re


def findNouns(text):

    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)

    #get nouns
    nounsList = list()
    regexNN = re.compile('NN|NNS')
    for tag in tagged:
        if regexNN.search(tag[1]):
            nounsList.append(tag[0])

    return nounsList

