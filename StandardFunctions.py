def WarningMessage():
    print("This program can't handle wrong input!")
    print("The filepath should only contain UTF-8 characters")
    print("If the filename after the rename already exists, all files until this file will be renamed and the program wil stop!")
    print("If a file contains the string two times in the name, both will be replaced!")
    print("Be sure to make a Backup of your files!")
    print("-------------------\n")

def InputFunction(message, inputType):
    print(message)
    x = None
    while type(x) != type(inputType):
        print("A ", type(inputType), " is required!")
        x = input()
        try:
            x = type(inputType)(x)
        except:
            print("Wrong input")
    return x

def OutputDirectoryFiles(message, warningMessage, dirFiles):
    print(message)
    print(dirFiles)
    print(warningMessage)

def ReturnPartOfString(string, splitSign, returnPart):
    for counter in range(len(string) - 1, 0, -1):
        if string[counter] == splitSign:
            if returnPart == '1':
                fileEnding = string[:counter]
            elif returnPart == '2':
                fileEnding = string[counter:]
            return fileEnding