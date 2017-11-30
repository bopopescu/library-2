from Search.FindSkills import *
#from Search.FindSkills1 import *

def main():
    skills_file = open('/home/gary/PycharmProjects/Resume/jobDescriptions/uber_software_engineer.txt', 'r')
    parseSkills = findSkills(skills_file.read())
    for p in parseSkills:
        print (p)


    #result = addskill(file)
    skills_file.close()


if __name__ == "__main__": main()

