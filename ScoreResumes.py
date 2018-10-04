import math

class ScoreResumes:

    def __init__(self, JobDescrpNouns, ResumeNouns):

        joblist = list()
        for job in JobDescrpNouns:
            joblist.append(job['tagged'])

        reslist = list()
        for res in ResumeNouns:
            reslist.append(res['tagged'])

        self.jdlist = joblist
        self.reslist = reslist


    def getResScore(self):

        jdNounList = self.jdlist
        resumeNounList = self.reslist
        wordList = []

        for jdNoun in jdNounList:

            for resNoun in resumeNounList:

                if jdNoun.lower() == resNoun.lower():

                    if wordList:
                        flag = False

                        for x in range(len(wordList)):

                            wordInList = wordList[x]

                            if wordInList['word'] == resNoun:

                                count = wordInList['count']
                                count = count + 1
                                wordList[x] = {'word': wordInList['word'], 'count': count}
                                flag = True

                        if not flag:

                            wordList.append({'word': resNoun, 'count': 1 })
                    else:

                        wordList.append({'word': resNoun, 'count': 1})

        return wordList


    def getList(self):
        list = []

        for nounsList in self.reslist: #{'nouns':listofnouns, 'filename': filename}
            wordList = []
            for noun in nounsList['nouns']:

                for jdNoun in self.jdlist:

                    if noun.lower() == jdNoun.lower():

                        if wordList:
                            flag = False

                            for x in range(len(wordList)):
                                wordInList = wordList[x]

                                if wordInList['word'] == noun:
                                    count = wordInList['count']
                                    count = count + 1
                                    wordList[x] = {'word': wordInList['word'], 'count': count,
                                                   'filename': nounsList['filename']}
                                    flag = True
                                if not flag:
                                    wordList.append({'word': noun, 'count': 1})

                        else:
                            wordList.append({'word': noun, 'count': 1})

            list.append({'list':wordList, 'filename':nounsList['filename']})

        return list

def resScores(wordList, count):

    ct = 1.0 * count
    subTotal = 1.0
    score = float()
    for jdWord in wordList:
        ct = jdWord['count']
        num = 1.0 * ct
        subTotal = subTotal + abs(math.log10(num/count))

    scr = subTotal
    score = round(scr, 2)

    return score


def getScores(maplist, totalJDNouns):

    #scoresList = PriorityQueue()
    scoreList = []
    tdnouns = totalJDNouns
    #get first node from mapList

    for nounList in maplist: #{'word': noun, 'count': 1, 'filename':nouns['filename']}
        subTotal = 1.0
        filename = nounList['filename']
        for noun in nounList['list']:
            num = 1.0 * noun['count']
            subTotal =  subTotal * (num/tdnouns)

        scr = abs(math.log10(subTotal))
        score = round(scr,3)

        #scoresList.push({'filename':filename,'score':score}, score)
        scoreList.append({'filename':filename,'score':score})

    return scoreList


def toString(tally):
    list = []

    while not tally.isEmpty():
        item = tally.pop()
        list.append(item)

    list.reverse()
    return list
