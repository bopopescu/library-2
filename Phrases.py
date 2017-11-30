from N_Gram import *

def phrases(text, wordlist):
    lines = text.split('\n')
    regexVB = re.compile('VB$|NN$|JJ$')
    #regexVB = re.compile('JJ$')
    regexNN = re.compile('NN|NNS')
    #procedure below provides phrases from job description
    nlist = list()
    for line in lines:

        sentence = nltk.word_tokenize(line)
        tagged = nltk.pos_tag(sentence)

        # print (line)
        for word in wordlist:

            # print ('SET')
            x = 0
            for it in tagged:
                x += 1
                if word['tagged'] == it[0]:
                    for t in tagged[x:len(tagged)]:
                        x += 1
                        if regexVB.match(t[1]):
                            item = []
                            # item.append(it)
                            # print ('VB: ',it)
                            x += 1
                            for t in tagged[x:len(tagged)]:
                                # item.append(t)
                                if regexNN.match(t[1]):
                                    # print ('NN: ',t)
                                    item = (it, t)
                                    nlist.append(item)
                                    break
                                x += 1
                        else:
                            x += 1

    return nlist