import os
from StandardFunctions import *

def ReplaceContentLogic(filePath, dirFiles, replaceFinder, replaceString):
    for oldFileName in dirFiles:
        for i in range(0, len(replaceFinder), +1):
            if replaceFinder[i] in oldFileName:
                newFileName = oldFileName.replace(replaceFinder[i], replaceString)
                oldFile = os.path.join(filePath, oldFileName)
                newFile = os.path.join(filePath, newFileName)
                os.rename(oldFile, newFile)
                oldFileName = newFileName

def ReplaceContentFillVariables():
    WarningMessage()

    filePath = InputFunction("Give in Filepath where the files are: ", "")
    if os.path.exists(filePath):
        dirFiles = os.listdir(filePath)
        OutputDirectoryFiles("These are all Files in this directory: ",
                             "If this is the wrong directory, close the program and restart!", dirFiles)
        replaceFinder = [InputFunction("Give in the the string which the files you want to rename contains: ", "")]
        addToFinder = InputFunction("Do you want to add another string to get replaced? yes = 1 | no = 2: ", 1)
        while addToFinder == 1:
            replaceFinder.append(InputFunction("Give in the the string which the files you want to rename contains: ", ""))
            addToFinder = InputFunction("Do you want to add another string to get replaced? yes = 1 | no = 2: ", 1)

        replaceString = InputFunction("Give in the string which replaces the string searched for: ", "")
        ReplaceContentLogic(filePath, dirFiles, replaceFinder, replaceString)

        dirFiles = os.listdir(filePath)
        OutputDirectoryFiles("These are the renamed Files in the directory: ", "Thanks for using ^^", dirFiles)
    else:
        print("Filepath doesn't exists!")