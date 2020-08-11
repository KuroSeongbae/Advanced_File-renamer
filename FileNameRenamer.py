import os
from StandardFunctions import *

def CreateFileNumber(fileCounter, numberAmount):
    strFileCounter = str(fileCounter)
    if len(strFileCounter) >= int(numberAmount):
        return strFileCounter
    else:
        fileNumberFill = int(numberAmount) - (len(strFileCounter))
        fileNumber = ''
        for i in range(fileNumberFill):
            fileNumber += '0'
        fileNumber += strFileCounter
        return fileNumber

def RenameFilesLogic(filePath, dirFiles, replaceString, wayOfCounting, numberAmount, fileNumberPosition, fileNumberSeparation):
    if wayOfCounting == '1':
        fileCounter = 1
    elif wayOfCounting == '2':
        fileCounter = len(dirFiles)
    else:
        fileCounter = 0;
    for oldFileName in dirFiles:
        fileEnding = ReturnPartOfString(oldFileName, '.', '2')
        if fileEnding is None:
            fileEnding = ''
        fileNumber = CreateFileNumber(fileCounter, numberAmount)
        oldFile = os.path.join(filePath, oldFileName)
        if fileNumberPosition == '1':
            if fileNumberSeparation == ':':
                newFile = os.path.join(filePath, '(' + fileNumber + ')' + replaceString + str(fileEnding))
            else:
                newFile = os.path.join(filePath, fileNumber + fileNumberSeparation + replaceString + str(fileEnding))
        elif fileNumberPosition == '2':
            if fileNumberSeparation == ":":
                newFile = os.path.join(filePath, replaceString + '(' + fileNumber + ')' + str(fileEnding))
            else:
                newFile = os.path.join(filePath, replaceString + fileNumber + fileNumberSeparation + str(fileEnding))
        else:
            print("Give in a valid option!")
        os.rename(oldFile, newFile)
        if wayOfCounting == '1':
            fileCounter += 1
        elif wayOfCounting == '2':
            fileCounter -= 1
        else:
            fileCounter += 1

def RenameFilesFillVariables():
    filePath = ("Give in Filepath where the files are: ", "")
    if os.path.exists(filePath) or os.walk(filePath):
        dirFiles = os.listdir(filePath)
        OutputDirectoryFiles("These are all Files in this directory: ",
                             "If this is the wrong directory, close the program and restart!", dirFiles)
        replaceString = InputFunction("Give in the string which will be the main filename: ", "")
        numberAmount = InputFunction("How many digits should your number have?: ", "")
        wayOfCounting = InputFunction("Do you want to count upwards (1) or downwards (2)?: ", "")
        fileNumberPosition = InputFunction("Should the number be at begin (1) or at end (2) of the filename?: ", "")
        fileNumberSeparation = InputFunction("Give in a valid Symbol, which seperates the filenumber from the filename. Type ':' to put the number in brackets (space can be used too): ", "")
        RenameFilesLogic(filePath, dirFiles, replaceString, wayOfCounting, numberAmount, fileNumberPosition, fileNumberSeparation)
    else:
        print("Filepath doesn't exists!")