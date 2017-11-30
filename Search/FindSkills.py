import re
import nltk
from Search.RemoveDuplicates import *


def findSkills(text):
    skillslist = open('/home/gary/PycharmProjects/Resume/jobskills/skills/skills.txt', 'r')
    skillslines = skillslist.read().split('\n')

    txtlines = text.split('\n')
    retlist = set()

    for ln in skillslines:
        reg = '\\b'+ln+'\\b'
        regex = re.compile(reg)

        for line in txtlines:
            matchSkill = regex.search(line)

            if matchSkill:
                match = matchSkill.group(0)
                retlist.add(match)

    #remove duplicate skills
    finallist = removeDups(retlist)

    return finallist
