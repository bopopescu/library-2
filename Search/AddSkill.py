import nltk


def addskill(file):
    try:
        tokens = nltk.word_tokenize(file.read())
        flag = True
        textToAdd = set()
        for token in tokens:
            textToAdd.add(token)

        while flag:
            text = input("Enter Skill: ")
            if text in textToAdd:
                print(text, "exists in Skills Dictionary")

            if text == '3':
                flag = False

            else:
                print(text, "does NOT exist in Skills Dictionary")
                response = input("Press Enter, 2 Skip, 3 to Quit?")
                if response == '':
                    textToAdd.add(text)
                elif response == '3':
                    flag = False

        addToFile = open('/home/gary/PycharmProjects/Resume/jobskills/skills/skills.txt', 'w')
        strFile = ''
        for skill in textToAdd:
            strFile = strFile + '\n' + skill

        addToFile.write(strFile)

        # close open resources
        addToFile.close()

        return True

    except Exception as e:
        return False