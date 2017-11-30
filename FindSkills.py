import re
import nltk


def findSkills(text):
    skillslist = open('/home/gary/PycharmProjects/Resume/jobskills/skills/skills.txt', 'r')
    skillslines = skillslist.read().split('\n')

    txtlines = text.split('\n')
    retlist = list()
    #compare each line of from text with regex list above
    for skline in skillslines:
        ct = txtlines.count(skline)
        if ct > 0:
            retlist.append(skline)

    return retlist

