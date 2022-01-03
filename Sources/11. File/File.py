import os; os.system('cls')

#-- open file ------------------------------------------------------------------
try:
    file = open('f:\MyFile.txt', 'a')
except IOError:
    file = None
    print("Open Error")

#-- write file -----------------------------------------------------------------
try:
    if (file != None):
        file.write("Hello world hello!\n")
        file.flush
except IOError:
    print("Write Error")

#-- close file -----------------------------------------------------------------
try:
    if (file != None):
        file.close()
        file = None
except IOError:
    print("Close Error")
