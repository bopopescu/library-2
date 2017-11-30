from employment import *
import re

class experience:

    def __init__(self, textLines):
        self.textLines = textLines

    def parseEmployment(self):

        textLines = self.textLines
        expList = []
        i = 0
        while i < len(textLines):
            line = textLines[i]
            if line:
                foundDate = isItADate(line)  # does this line contain a date
                if foundDate[0]:  # if it does contain a date
                    empText = employmentText(foundDate[1], i, textLines)
                    i = empText['num'] - 1
                    expList.append(empText)
            i += 1

        return expList

#method stores experience data in object
def employmentText(date, lineNum, textLines):
    flag = False
    line = ""
    num = lineNum + 1
    if num >= len(textLines) or len(textLines) is None:
        return False

    while not flag:
        ln = textLines[num]
        eof = False
        if ln:
            eof = endOfExperience(ln)
            found = isItADate(ln)
            if not found[0]:
                line = line + "\n" + ln
                num += 1

            else:
                flag = True
        num += 1
        if num >= len(textLines) or eof:
            flag = True

    entry = {'date': date, "line": line, "num":num} #employment(date, line, num)

    return entry


#start of experience section
def startOfExperience(line):
    if line:
        regexStartOfExp = ["Experience|EXPERIENCE|HISTORY|History|Work History|WORK HISTORY|" \
                      "Work Experience|WORK EXPERIENCE"]

        regex = re.compile(regexStartOfExp[0])
        matchObj = regex.search(line)
        if matchObj:
            return True
        else:
            return False


#end of experience section
def endOfExperience(line):
    regexEndOfExp = "Skills|SKILLS|Education|EDUCATION|Other|OTHER|References|REFERENCES|Volunteer|VOLUNTEER"
    if line:
        regex = re.compile(regexEndOfExp)
        result = ""
        if regex.search(line):
            return True
        else:
            return False


# verify regex DATE
def isItADate(line):
    if line:

        regexDateString = ["[A-Z]\\w{2,10}\\s\\d{2,4}\\s\\D{1,2}\\s[A-Z]\\w{2,10}\\s\\d{2,4}|"
                           "\\d{4}[/|-]\\d{4}\\s\\D{1,2}\\s\\d{4}[/|-]\\d{4}|\\d{4}\\s[/|-]\\s\\d{4}|"
                           "\\d{4}-\\d{4}|\\d{2}[/|-| ]\\d{4}\\D{1,2}\\d{2}[/|-| ]\\d{4}|"
                           "[A-Z]\\w{2,10}\\s\\d{2,4}\\s\\S{1,2}\\s((Present)|(Current))|"
                           "\\d{1,2}\\S\\d{2,4}\\s\\D{1,2}\\s\\d{1,2}\\S\\d{2,4}"]
                            #"[A-Z]\\w{2,10}\\s{1,2}[/|-]\\s{1,2}[A-Z]\\w{2,10}"]


        regex = re.compile(regexDateString[0])
        matchObj = regex.search(line)
        if matchObj:#regex.search(line):
            match = matchObj.group()
            return [True,match]
        else:
            return [False,0]



