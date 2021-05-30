import os
import shutil
# Program copy all files from one location to another
"""
scr_location = "C:\\Testdata\\test_folder"
tag_location = "E:\\Filesdata"

#1. get list of files and folder from  source location, os.listdir(path)
#2. iterate through each files and folder using loop
#3. create path for each file/folder using os.path.join(src_path, item)
#4. check item path is file or folder os.path.isdir(item_path) or os.path.isfile(item_path)
#5. if we get tru to file path then copy fril from source to destination : shutil.copy(src, tar)

#1. get list of files and folder from  source location, os.listdir(path)
data_list = os.listdir(scr_location)

#2. iterate through each files and folder using loop
for item in data_list:
    #print(item)
    # check item is file/folder
    # 3. create path for each file/folder using os.path.join(src_path, item)
    item_path = os.path.join(scr_location, item)

    # 4. check item path is file or folder os.path.isdir(item_path) or os.path.isfile(item_path)
    if os.path.isfile(item_path):
        print(item)

        # 5. if we get tru to file path then copy file from source to destination : shutil.copy(src, tar)
        shutil.copy(item_path, os.path.join(tag_location))
    else:
        continue

"""

# Create a small backup solution to copy all specific extension file in specific folder only.

#Steps
#1 -> Get all files and folder list : os.listdir(src_path)
#2 -> Itrate through each items in the list using loop.
#3 -> create path of each item os.path.join(scr_path, item)
#4 -> check if given path id file or folder
#5 -> if it is file then get a extension of file
#6 -> create extension folder on target and copy the file.

scr_loc = "C:\\Testdata\\test_folder"
tag_loc = "E:\\filedata2"

#1 -> Get all files and folder list : os.listdir(src_path)
listdata = os.listdir(scr_loc)

#2 -> Iterate through each items in the list using loop.
for item in listdata:
    # 3 -> create path of each item os.path.join(scr_path, item)
    item_path = os.path.join(scr_loc, item)

    #4 -> check if given path id file or folder
    if os.path.isfile(item_path):

        # 5 -> if it is file then get a extension of file
        file_ext = item.split(".")[1]

        #6 -> create extension folder on target and copy the file.
        tag_dir = os.path.join(tag_loc, file_ext)

        if os.path.isdir(tag_dir):
            shutil.copy(item_path, os.path.join(tag_dir, item))
        else:
            os.mkdir(tag_dir)
            shutil.copy(item_path, os.path.join(tag_dir, item))




"""
Get file extension

>>> filename = "testfile.txt"
>>> filename.split(".")
['testfile', 'txt']
>>> filename.split(".")[1]
'txt'
>>>"""






