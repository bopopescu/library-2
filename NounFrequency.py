import decimal
import random

from nltk.stem.porter import *

from Graphs.util import PriorityQueue
from resumeUpdate import *


def nounFrequence(text):
    # stem
    jdstemmer = PorterStemmer()
    jdtokens = nltk.word_tokenize(text)
    jdStmOrg = []
    for tokes in jdtokens:
        original = tokes
        #print('ORIGINAL: ', tokes)
        jdstemmed = jdstemmer.stem(tokes)
        jdStmOrg.append({'stemmed':jdstemmed, 'original':original})
        #print("Stemmed: ", jdstemmed, " Orginal: ", original)

    # get dups

    # remove duplicates
    # noDups = list(set(jdstemmed))
    # tag words
    taggedList = []
    for tag in jdStmOrg:
        original = tag['original']
        lst = []
        lst.append(tag['stemmed'])
        jdTagged = nltk.pos_tag(lst)
        taggedList.append({'tagged':jdTagged, 'original':original})
        #print ("Tagged: ", jdTagged, " ORGINAL: ", tag['original'])

    saveJD = []
    saveList = []
    p = re.compile('NN|NNS|NNP|NNPS|PRP|PRP$|WP|WP$')
    # print ('GET JD NOUNS')
    for tag in taggedList:
        t = (tag['tagged'])[0]
        #print (t)
        original = tag['original']

        if p.match(t[1]):
            # print(tag[0])
            saveJD.append({'tagged':t[0], 'original':original})
            saveList.append(t[0])
            #print ("TAGGED: ", t[0], " ORIGINAL: ", original)

    # count duplicate nouns
    wordCount = []
    x = 0

    for s, z in zip(saveJD, saveList):
        original = s['original']
        count = saveList.count(s['tagged'])

        if count is not 0:
            wordCount.append({'tagged': s['tagged'], 'count': count, 'original': original})



    # remove duplicate entries
    seen = set()
    new_list = []
    for d in wordCount:
        t = d['tagged']
        if t not in seen:
            seen.add(t)
            new_list.append(d)

    # ascending order
    priorityqueue = PriorityQueue()
    for item in new_list:
        count = 0.0
        count = count + item['count']
        if count > 0:
            rd = float(decimal.Decimal(random.randrange(1, 1389000)) / 10000000)
            ct = count + rd
            # print (ct)
            priorityqueue.push(item, ct)

    finalList = []
    while not priorityqueue.isEmpty():
        popped = priorityqueue.pop()
        item = popped[1]
        finalList.append(item)

    #for item in finalList:
        #print("TAGGED: ", item['tagged'], " COUNT: ", item['count'], " ORIGINAL: ", item['original'])

    finalList.reverse()

    return finalList


def nounFreqNoStem(text):
    text = text.lower()
    jdtokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(jdtokens)

    saveJD = []
    saveList = []
    p = re.compile('NN$|NNS$|NNP$|NNPS$|PRP$|PRP$|WP$|WP$')
    # print ('GET JD NOUNS')
    for tag in tagged:
        if p.match(tag[1]):
            saveJD.append(tag)

    # count duplicate nouns
    wordCount = []
    x = 0
    for sword in saveJD:
        count = saveJD.count(sword)
        if count is not 0:
            wordCount.append({'word':sword, 'count':count})

    # remove duplicate entries
    seen = set()
    new_list = []
    for d in wordCount:
        t = d['word']
        if t not in seen:
            seen.add(t)
            new_list.append(d)

    # ascending order
    priorityqueue = PriorityQueue()
    for item in new_list:
        count = 0.0
        count = count + item['count']
        if count > 0:
            rd = float(decimal.Decimal(random.randrange(1, 1389000)) / 10000000)
            ct = count + rd
            # print (ct)
            priorityqueue.push(item, ct)

    finalList = []
    while not priorityqueue.isEmpty():
        popped = priorityqueue.pop()
        item = popped[1]
        finalList.append(item)

        # for item in finalList:
        # print("TAGGED: ", item['tagged'], " COUNT: ", item['count'], " ORIGINAL: ", item['original'])

    finalList.reverse()

    return finalList