import os, sys
import names
from shutil import copyfile


def duplicateFiles(path, num):
    os.chdir(path)

    for file in os.listdir(path):
        for x in range(0, num):
            name = names.get_full_name()
            spName = file.split(".")
            nName = name + '.' + spName[1]
            newFile = open(nName, 'rb')
            newFile.write(file)



def changeFileName(directory, loops):
    path = directory
    os.chdir(path)
    for file in os.listdir(path):
        for x in range(0, loops):
            name = names.get_full_name()
            spName = file.split(".")
            nName = name + '.' + spName[1]
            os.rename(file, nName)




