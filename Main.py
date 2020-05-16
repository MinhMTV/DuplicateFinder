import FileLib as f
import time
import os
import re
from datetime import datetime


#get currentTime, format: 16/05/2020, 05:30:58
def getTime():
    return datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

indicator = "(1)"
CpyFldName = "Double_Images"
scrImgList = []
log = "log"

#Creates a LogFile for the Copy and remove Process
#@logpath LogFilePath
#@newFil number of new copied files
#@exFil number of files that already existed in dir
#@NrsaFol number of duplicate Images that are not in the same Folder as original file
#@saFoldFil list of number of duplicate Images that are not in the same Folder as orginal file
#@NrImg nr of total Images in new created Folder
#@fwoOrg List of File w/o Original File
#@NrFwoOrg nr of Files w/o Original File
#@NrRmFil Nr of removed Files
#@rmFil List of Removed Files
def Cpylog(logpath,newFil,exFil,NrsaFol,saFoldFil,NrImg,FwoOrg,NrFwoOrg,NrRmFil,rmFil):
    f.writeText(logpath,getTime() + f" {newFil} New Files were copied")
    f.writeText(logpath,getTime() + f" {exFil} Files already existed")
    f.writeText(logpath,getTime() + f" {NrsaFol} duplicate Files are not in the same folder as original\n")
    f.writeText(logpath,saFoldFil)
    f.writeText(logpath,getTime() + f" {NrImg} total Images are in the directory\n")
    f.writeText(logpath,getTime() + f" These duplicates dont have an original file\n")
    f.writeText(logpath,FwoOrg)
    f.writeText(logpath,getTime() + f" There is a total of {NrFwoOrg} files without original file. They weren't copied\n")
    f.writeText(logpath,getTime() + f" A total of {NrRmFil} files were removed\n")
    f.writeText(logpath,rmFil)

def takePath():
    while True:
        answer = input(
            "You want to enter specific path to compare all files?\nY/N\n")
        if answer.lower() == 'y':
            time.sleep(1)
            path = input("Enter specific path now\n")
            filepath = path.replace('"', "")
            if os.path.exists(filepath):
                print("Path exist")
                path = filepath
                return path
            else:
                print("Invalid Path. Please try again\n")

        elif answer.lower() == 'n':
            print("Path will be the same directory than the Script File")
            path = os.path.dirname(os.path.realpath(__file__))
            print(path)
            return path
        else:
            print("Invalid Input. Please Enter Y / N\n")

def main():
    path = takePath()
    imageList = f.getAllImages(path)
    f.getAllImageExt(path, imageList)
    duImageList = f.findDuplicateImagesByInd(path,imageList,indicator)
    os.chdir(path)
    os.chdir("..")
    homePath = os.curdir
    print("root path: " + os.getcwd())
    for Image in imageList:
        for x in Image:
            scrImgList.append(x)

    filewOrg = f.checkDuplicateByEndInd(duImageList,scrImgList,indicator)
    samefolder = f.checkDupInSameFold(duImageList,scrImgList,indicator)
    copy = f.copyFiles(homePath,CpyFldName,duImageList,imageList,indicator,filewOrg)
    temp = os.getcwd() + copy[0].replace(".","")
    print("write Data into LogFile")
    logpath = os.path.join(copy[0],log +".txt")
    f.removeFiles(copy[1][0])
    if os.path.exists(logpath):
        os.remove(logpath)
        print("override file")
        Cpylog(logpath,copy[2][0],copy[2][1],len(samefolder[1]),samefolder[1],f.getNrofImages(copy[0]),copy[1][1],len(copy[1][1]),len(copy[1][0]),copy[1][0])
    else:
        Cpylog(logpath,copy[2][0],copy[2][1],len(samefolder[1]),samefolder[1],f.getNrofImages(copy[0]),copy[1][1],len(copy[1][1]),len(copy[1][0]),copy[1][0])

if __name__ == '__main__':
    main()
