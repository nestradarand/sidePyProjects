import os
import shutil

# def moveAllFiles(dir,pdfDir,wordDir):
#     for thing in os.listdir(dir):
#         extension = os.path.splitext(thing)
#         fileType = extension[1]
#         firstPath = dir + "/"+thing
#         if(fileType == ".pdf"):
#             path = os.path.dirname(thing)
#             pdfPath = pdfDir + "/" + thing
#             os.rename(firstPath,pdfPath)
#         if(fileType == ".docx"):
#             path = os.path.dirname(thing)
#             worthPath = wordDir + "/" + thing
#             os.rename(firstPath,wordPath)

def moveAllFiles(firstDir,fileType,destDir):
    for thing in os.listdir(firstDir):
        extension = os.path.splitext(thing)
        file_extension = extension[1]
        if(file_extension == fileType):
            firstPath = firstDir + "/"+thing
            newPath = destDir + "/" + thing
            os.rename(firstPath,newPath)

moveAllFiles("C:/Users/noahe/Downloads",".pdf","C:/Users/noahe/Desktop/pdfDownloads")
moveAllFiles("C:/Users/noahe/Downloads",".docx","C:/Users/noahe/Desktop/wordDownloads")
        
