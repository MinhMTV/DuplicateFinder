import os
from os import walk
from os.path import isfile, join
import pathlib
import timeit
import time
import glob


valid_images = ["ase", "art", "bmp", "blp", "cd5", "cit", "cpt", "cr2", "cut", "dds", "dib", "djvu", "egt", "exif", "gif", "gpl", "grf", "icns", "ico", "iff", "jng", "jpeg", "jpg", "jfif", "jp2", "jps",
                "lbm", "max", "miff", "mng", "msp", "nitf", "ota", "pbm", "pc1", "pc2", "pc3", "pcf", "pcx", "pdn", "pgm", "PI1", "PI2", "PI3", "pict", "pct", "pnm", "pns", "ppm", "psb", "psd", "pdd",
                "psp", "px", "pxm", "pxr", "qfx", "raw", "rle", "sct", "sgi", "rgb", "int", "bw", "tga", "tiff", "tif", "vtf", "xbm", "xcf", "xpm", "3dv", "amf", "ai", "awg", "cgm", "cdr", "cmx",
                "dxf", "e2d", "egt", "eps", "fs", "gbr", "odg", "svg", "stl", "vrml", "x3d", "sxd", "v2d", "vnd", "wmf", "emf", "art", "xar", "png", "webp", "jxr", "hdp", "wdp", "cur", "ecw",
                "iff", "lbm", "liff", "nrrd", "pam", "pcx", "pgf", "sgi", "rgb", "rgba", "bw", "int", "inta", "sid", "ras", "sun", "tga"
                ]

valid_videos = ["3g2", "3gp", "aaf", "asf", "avchd", "avi", "drc", "flv", "m2v", "m4p", "m4v", "mkv", "mng", "mov", "mp2", "mp4", "mpe", "mpeg", "mpg", "mpv", "mxf", "nsv", "ogg", "ogv", "qt", "rm",
                "rmvb", "roq", "svi", "vob", "webm", "wmv", "yuv"
                ]


def getListofFolders(path):
    list_subfolders_with_paths = [
        f.path for f in os.scandir(path) if f.is_dir()]
    print("There are " + str(len(list_subfolders_with_paths)) +
          " SubFolder in this Folder")
    print(type(list_subfolders_with_paths))
    for x in list_subfolders_with_paths:
        print(x)


def getListofFiles(path):
    onlyfiles = [f for f in os.listdir(path) if isfile(join(path, f))]
    print(onlyfiles)


def getFilAndDirPath(path):
    f = []
    for (dirpath, dirnames, filenames) in walk(path):
        f.append(dirpath)
        for y in dirnames:
            f.append(os.path.join(dirpath, y))
        for x in filenames:
            f.append(os.path.join(dirpath, x))
        # for name in filenames:
        #     print(os.path.join(dirpath, name))
        break


def getAllImages(path):
    f = []
    count = 0
    tic = time.perf_counter()
    for x in valid_images:
        temp = glob.glob(path + '/**/*.' + x, recursive=True)
        if len(temp) > 1:
            f.append(temp)
    toc = time.perf_counter()
    print(f"Get all Images in {toc - tic:0.4f} seconds")
    for lists in f:
        count += len(lists)
    print("There are " + str(count) +
          " Images in this Folder")
    return f


# my_path/     the dir
# **/       every file and dir under my_path
# *.txt     every file that ends with '.txt'


def getspecificFileExtension(path):
    userExt = input("Which File extensions do you want to check?\n")
    files = glob.glob(path + '/**/*.' + userExt, recursive=True)
    if not files:
        print("no files with " + userExt + " found")
    else:
        for x in files:
            print(x)
        print("There are " + str(len(files)) + " Files with ." + userExt)
    reCheck = input("\nDo you want to check other extensions?\nY/N\n")
    if reCheck.lower() == 'y':
        getspecificFileExtension(path)

    elif reCheck.lower() == 'n':
        print("Programm will end")
    else:
        print("Invalid Input. Please Enter Y / N\n")
        getspecificFileExtension(path)


def getAllFileExtension(path):
    ListFiles = walk(path)
    SplitTypes = []
    for walk_output in ListFiles:
        for file_name in walk_output[-1]:
            if file_name.split(".")[-1] not in SplitTypes:
                SplitTypes.append(file_name.split(".")[-1])
    print(SplitTypes)


def getAllImageExt(path, ImageList):
    SplitTypes = []
    for images in ImageList:
        for file_name in images:
            if file_name.split(".")[-1] not in SplitTypes:
                SplitTypes.append(file_name.split(".")[-1])
    print(SplitTypes)

# def main():
#     path = takePath()
#     getAllImageExt(path, getAllImages(path))

# if __name__ == '__main__':
#      main()
