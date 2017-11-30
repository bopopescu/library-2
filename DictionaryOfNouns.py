import nltk
import re
from nltk.stem.porter import *

def dictionary(text):
    # get dictionary of terms

    tokenDic = nltk.word_tokenize(text)
    #remove duplicates
    seen = set()
    new_dict = []
    for d in tokenDic:
        t = d
        if t not in seen:
            seen.add(t)
            new_dict.append(d)

    #create stemmer instance
    stemmer = PorterStemmer()
    stemmed = list()
    #stem tokens
    for token in new_dict:
        stemDic = stemmer.stem(token)
        stemmed.append(stemDic)

    taggedDic = nltk.pos_tag(stemmed)

    # get only the nouns from taggedDic
    dict = list()
    regexNouns = re.compile('NN|NNS|NNP|NNPS')
    for tag in taggedDic:
        if regexNouns.match(tag[1]):
            dict.append(tag[0])

    return dict