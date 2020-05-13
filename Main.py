import FileLib as f
import time
import os
import re

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
    duImageList = f.findDuplicateImages(path,imageList,"(1)")
    os.chdir(path)
    os.chdir("..")
    homePath = os.curdir
    print(os.getcwd())
    f.copyFiles(homePath,"copies",duImageList)


if __name__ == '__main__':
    main()
