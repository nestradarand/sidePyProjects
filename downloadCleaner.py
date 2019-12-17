import os


def switchPaths(firstDir,secondDir,name):
    firstPath = firstDir + "/" + name
    newPath = secondDir + "/" + name
    os.rename(firstPath,newPath)

def moveFilesToDesktop(firstDir):
    for thing in os.listdir(firstDir):
        extension = os.path.splitext(thing)
        file_extension = extension[1]
        if(file_extension == ".pdf"):
            switchPaths(firstDir,"C:/Users/noahe/Desktop/pdfDownloads",thing)
        elif(file_extension == ".docx") or (file_extension == ".doc"):
            switchPaths(firstDir,"C:/Users/noahe/Desktop/wordDownloads",thing)
        elif(file_extension == ".JPG") or (file_extension == ".png") or (file_extension == ".MP4"):
            switchPaths(firstDir,"C:/Users/noahe/Desktop/visualDownloads",thing)
        elif(file_extension == ".pptx"):
            switchPaths(firstDir,"C:/Users/noahe/Desktop/pptDownloads",thing)
        else:
            switchPaths(firstDir,"C:/Users/noahe/Desktop/otherDownloads",thing)


