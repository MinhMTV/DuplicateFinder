import os
import pathlib
import timeit
import glob

def takePath():
    answer = input("You want to enter specific path to compare all files?\nY/N\n")
    if answer.lower() == 'y' :
        path = input("Enter specific path now\n")
        filepath = path.replace('"', "")
        if os.path.exists(filepath):
            print("Path exist")
            path = filepath
        else:
            print("Invalid Path. Please try again\n")
            takePath()

    elif answer.lower() == 'n':
        print("Path will be the same directory than the Script File")
        path = os.path.dirname(os.path.realpath(__file__))
        print(path)
    else:
        print("Invalid Input. Please Enter Y / N\n")
        takePath()
    return path

def getListofFolders(path):
    print(path)
    list_subfolders_with_paths = [
        f.path for f in os.scandir(path) if f.is_dir()]
    print("There are " + str(len(list_subfolders_with_paths)) + " SubFolder in this Folder")
    print(list_subfolders_with_paths)
    for x in list_subfolders_with_paths:
        print(x)


if __name__ == '__main__':
    path = takePath()
    getListofFolders(path)
