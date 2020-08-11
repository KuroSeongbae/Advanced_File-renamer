import os
from StandardFunctions import *

def ChangeFileExtensionLogic(filePath, dirFiles, addOrRename, extensionName):
    if addOrRename == '1':
        for oldFileName in dirFiles:
            oldFile = os.path.join(filePath, oldFileName)
            newFile = os.path.join(filePath, oldFileName + extensionName)
            os.rename(oldFile, newFile)
    elif addOrRename == '2':
        for oldFileName in dirFiles:
            newFileName = ReturnPartOfString(oldFileName, '.', '1')
            oldFile = os.path.join(filePath, oldFileName)
            newFile = os.path.join(filePath, newFileName + extensionName)
            os.rename(oldFile, newFile)

def ChangeFileExtensionFillVariables():
    filePath = InputFunction("Give in Filepath where the files are: ", "")
    if os.path.exists(filePath) or os.walk(filePath):
        dirFiles = os.listdir(filePath)
        OutputDirectoryFiles("These are all Files in this directory: ",
                             "If this is the wrong directory, close the program and restart!", dirFiles)
        addOrRename = InputFunction("Do you want to add (1) or overwrite (2) the extension?: ", "")
        extensionName = InputFunction("Give in the new extension (don't forget the dot): ", "")
        ChangeFileExtensionLogic(filePath, dirFiles, addOrRename, extensionName)

