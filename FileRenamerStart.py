from StandardFunctions import *
from FileNameRenamer import *
from FileNameContentReplacer import *
from FileNameExtensionNamer import *

programChoice = InputFunction("Choose the program you want to use: \n1: Rename Files \n2: Rename Content of Files \n3: Change file extension", 1)
if programChoice == 1:
    RenameFilesFillVariables()
elif programChoice == 2:
    ReplaceContentFillVariables()
elif programChoice == 3:
    ChangeFileExtensionFillVariables()
else:
    print("Give in a valid option.")