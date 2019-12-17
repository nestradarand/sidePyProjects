import os 
import sys
from pathlib import Path
import send2trash as Trasher
from time import gmtime, strftime


'''
This module is to be used to find the root of directories from the current one
and to comb through the files from a specified directory to find/rellocate files
'''

##works with recursion
def recursiveFiles(directory):
    for thing in os.listdir(directory):
        full_path = os.path.join(directory,thing)
        if os.path.isfile(full_path):
            print(thing)
        elif os.path.isdir(full_path):
            print("---New directory Found---")
            print(full_path)
            recursiveFiles(full_path)
####retuns time since epoch as [month,year]
def getLastOpenDate(path):
    lastTimeOpened = os.path.getatime(path)
    formatted = strftime("%m/%Y",gmtime(lastTimeOpened)).split("/")
    returner = [int(formatted[0]),int(formatted[1])]
    return returner

def earlierThan(new_Year,limit):
    # if not(int(new_Year[0]) < int(limit[0])):
    #     return False
    # elif not(int(new_Year[1]) < int(limit[1])):
    #     return False
    # else:
    #     return True
    return ( int(new_Year[0]) <= int(limit[0]) and int(new_Year[1]) < int(limit[1]))

####goes through all directories and relocates files based on when they were last opened
###takes the directory to look through and the month/year before which we want all files removed
def combThroughAndTrash(directory,search_limit):
    try:
        for thing in os.listdir(directory):
            try:
                full_path = (os.path.join(directory,thing))
                if os.path.isfile(full_path):
                    last_opened = getLastOpenDate(full_path)
                    extension = (os.path.splitext(thing))[1]
                    if(earlierThan(last_opened,search_limit)): 
                        if(extension == ".pdf"):
                            Trasher.send2trash(full_path)
                            print(thing + " moved to trash")
                        elif(extension == ".doc") or (extension == ".docx"):
                            Trasher.send2trash(full_path)
                            print(thing + " moved to trash")
                        elif(extension == ".ppt") or (extension == ".pptx"):
                            Trasher.send2trash(full_path)
                            print(thing + " moved to trash")
                        else:
                            continue
                elif os.path.isdir(full_path):
                    print("Moving to new directory: " + str(full_path))
                    combThroughAndTrash(str(full_path),search_limit)
            except Exception as e:
                print(e)
                print("Exception occurred trying to handle:" + full_path)
                print("Execution will continue")
                continue
    except Exception:
        print("A fatal exception occurred trying to comb through the directory: " + directory)
        sys.exit(0)

        
def getRoot(directory):
    try:
        curr_path = Path(directory)
        print("Current dir:" + str(curr_path))
        parent = curr_path.parent
        if (str(directory) == str(parent)):
            print("End reached")
            sys.exit(0)
        if(parent):
            getRoot(parent)
        else:
            print("End reached")
    except Exception:
        print("Error in attempting to use entered directory:" + str(directory))



def main():
    try:
        if(sys.argv[1] == 'r'):
            arg = sys.argv[1]
            if(arg == 'r'):
                getRoot(os.getcwd())
    except Exception:
        try:
            year = int(input("Enter the year you wish to set the deleting limit to: "))
            month = int(input("Enter the month you wish to set the deleting limit to: "))
            date_limit = [month,year]
            print("Do you want to use the current working directory to comb through?")
            theInput = int(input("Enter 1 for yes 0 for no: "))
            if(theInput == 1):
                combThroughAndTrash(os.getcwd(),date_limit)
            elif(theInput == 0):
                newDir = input("Enter new directory to use: ")
                combThroughAndTrash(newDir,date_limit)
            else:
                print("Invalid command entered")

        except Exception:
            print("Invalid information entered")


if __name__ == "__main__":
    main()