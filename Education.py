import nltk
import re


def education(text):
    regexInst = re.compile('University|College')
    regexDegree = re.compile('Bachelor|Master|Degree|Diploma|Certificate|University|College')
    file = open('/home/gary/PycharmProjects/Resume/education/degreetypes.txt', 'r')
    typeList = file.read().split()

    lines = text.split('\n')
    retlist = list()

    for line in lines:
        matchInst = regexInst.match(line)
        matchDegree = regexDegree.search(line)
        if  matchDegree:
            mtchDgr = matchDegree.group()
            retlist.append(mtchDgr)

    return retlist





