import nltk
import os

import docxpy
import nltk
from nltk.stem.porter import *

from PyPDF2 import PdfFileReader
from ScoreResumes import *


class combinedScores:

    def __init__(self, jobDescription, resume):

        self.resume = resume
        self.jobDescription = jobDescription
        self.saveResumeNouns = []
        self.saveJDNouns = []


    def getJobDescriptionNouns(self):
        jdTokens = nltk.word_tokenize(self.jobDescription)
        jdTagged = nltk.pos_tag(jdTokens)
        p = re.compile('N.*')
        saveJDNouns = []

        # store nouns from job description
        for tag in jdTagged:
            t = tag[1]
            if p.match(t):
                saveJDNouns.append(tag[0])

        return saveJDNouns


    def getResumeNouns(self):

        resumeNounsList = []

        for file in os.listdir(self.resume):
            if file.endswith(('.docx', '.pdf')):
                saveNouns = []
                if file.endswith('.pdf'):
                    PDF = PdfFileReader(open(file, 'rb'))
                    if PDF.isEncrypted:
                        decrypt = PDF.decrypt('')
                        if decrypt == 0:
                            print ("Password Protected PDF: " + file)
                            raise Exception("Nope")
                        elif decrypt == 1 or decrypt == 2:
                            print ("Successfully Decrypted PDF")

                    text = ''
                    for page in PDF.pages:
                        text = text + "\n" + page.extractText()

                    jdTokens = nltk.word_tokenize(text)
                    stemmer = PorterStemmer()
                    stemmed = [stemmer.stem(token) for token in jdTokens]
                    jdTagged = nltk.pos_tag(stemmed)

                    p = re.compile('NN|NNS|NNP|NNPS|PRP|PRP$|WP|WP$')
                    # store nouns from job description
                    for tag in jdTagged:
                        t = tag[1]
                        if p.match(t):
                            saveNouns.append(tag[0])

                else:
                    text = docxpy.process(file)
                    jdTokens = nltk.word_tokenize(text)
                    stemmer = PorterStemmer()
                    stemmed = [stemmer.stem(token) for token in jdTokens]
                    jdTagged = nltk.pos_tag(stemmed)
                    p = re.compile('NN|NNS|NNP|NNPS|PRP|PRP$|WP|WP$')

                    # store nouns from job description
                    for tag in jdTagged:
                        t = tag[1]
                        if p.match(t):
                            saveNouns.append(tag[0])

                resumeNounsList.append({'filename': file, 'list': saveNouns, 'text': text})

        return resumeNounsList


def scoreResumes(jdNouns, resumeNouns):
    #scoresList = PriorityQueue()
    scoresList= []
    for resNouns in resumeNouns:
        scoreRes = ScoreResumes(jdNouns, resNouns)
        score = scoreRes.getResScore()

        # get total frequency score
        logScore = resScores(score, len(jdNouns))
        #print ('File: ', resListOfNouns['filename'], 'LogScore: ',resTally)
        """
        # get part frequency score
        text = resListOfNouns['text'].split('\n')
        partScoresOfResume = experience(text)
        expList = partScoresOfResume.parseEmployment()
    
        #print (resListOfNouns['filename'])
        
        partScores = []
        for item in expList:
            resTokens = nltk.word_tokenize(item['line'])
            resTagged = nltk.pos_tag(resTokens)
            p = re.compile('N.*')
            saveRes = []
            # store nouns from job description
            for tag in resTagged:
                t = tag[1]
                if p.match(t):
                    saveRes.append(tag[0])

            scoreRes = ScoreResumes(saveJDNouns, saveRes)
            score = scoreRes.getResScore()
            partScore = resScores(score, len(saveJDNouns))
            partScores.append({'date':item['date'], 'score':partScore})
        """
        scoresList.append({'logscore': logScore})

    return scoresList

