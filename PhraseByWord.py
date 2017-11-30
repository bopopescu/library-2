import nltk
import re

def phraseByWord0(jobtext, jobList):
    phraseList = list()
    lines = jobtext.lower().split('\n')
    for line in lines:
        tokens = nltk.word_tokenize(line)
        taggedTokens = nltk.pos_tag(tokens)

        for word in jobList:
            ct = 0
            for taggedToken in taggedTokens:
                ct += 1
                if ct < len(taggedTokens):
                    phrase = []
                    if taggedToken[0] == word:
                        # print("Token: ", taggedToken[0], " Word: ", word)
                        ptct = ct - 2  # prior temp count number
                        ntct = ct
                        regex = re.compile('JJ|VGB|NN|NNS')
                        priorTagged = taggedTokens[ptct]
                        nextTagged = taggedTokens[ntct]

                        if regex.search(priorTagged[1]):
                            phrase = (priorTagged[0], word)
                        if regex.search(nextTagged[1]):
                            phrase = (word, nextTagged[0])

                        phraseList.append(phrase)

    tempList = list()
    for temp in phraseList:
        if temp:
            tempList.append(temp)

    seen = set()
    new_list = []
    for d in tempList:
        t = d
        if t not in seen:
            seen.add(t)
            new_list.append(d)

    return new_list


def phraseByWord1(text, wordList):

    phraseList = list()
    lines = text.lower().split('\n')
    for line in lines:
        tokens = nltk.word_tokenize(line)
        taggedTokens = nltk.pos_tag(tokens)

        for word in wordList:
            count = word['count']
            if count > 0:
                word = word['word'][0]
                #print ('WORD: ', word)
                ct = 0
                for taggedToken in taggedTokens:
                    ct += 1
                    if ct < len(taggedTokens):
                        phrase = []
                        if taggedToken[0] == word:
                            #print("Token: ", taggedToken[0], " Word: ", word)
                            ptct = ct - 2  # prior temp count number
                            ntct = ct
                            regex = re.compile('JJ|VGB|NN|NNS')
                            priorTagged = taggedTokens[ptct]
                            nextTagged = taggedTokens[ntct]

                            if regex.search(priorTagged[1]):
                                phrase = (priorTagged[0], word)

                            if regex.search(nextTagged[1]):
                                phrase = (word, nextTagged[0])

                            phraseList.append(phrase)

    tempList = list()
    for temp in phraseList:
        if temp:
            tempList.append(temp)

    seen = set()
    new_list = []
    for d in tempList:
        t = d
        if t not in seen:
            seen.add(t)
            new_list.append(d)

    return new_list