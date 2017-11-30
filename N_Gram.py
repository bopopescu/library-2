from nltk.util import ngrams
import nltk
import re

def n_gram(text):
    new_text = text.lower()
    lines = new_text.split('\n')
    bgrm = list()
    for line in lines:
        bgln = nltk.bigrams(line.split())
        bgrm.append(bgln)

    #bigram = list(nltk.bigrams(new_text.split()))
    #fdist = nltk.FreqDist(bigram)

    # for k, v in fdist.items():
    # print (k, v)
    tagList = list()
    for bi in bgrm:
        for i in bi:
            tag = nltk.pos_tag(i)
            regex = re.compile('NNS$|NN$')  # |NNP|NNPS|PRP|PRP$|WP|WP$')
            if regex.match(tag[0][1]) and regex.match(tag[1][1]):
                tagList.append(i)
                #print (tag)
    """
    for bi in bigram:
        tag = nltk.pos_tag(bi)
        regex1 = re.compile('NNS|NN$') #|NNP|NNPS|PRP|PRP$|WP|WP$')
        regex2 = re.compile('NN$')
        if regex1.match(tag[0][1]) and regex2.match(tag[1][1]):
            tagList.append(bi)
            print(tag)
    """
    fdist = nltk.FreqDist(tagList)
    #for k, v in fdist.items():
        #print(k, v)
    return fdist