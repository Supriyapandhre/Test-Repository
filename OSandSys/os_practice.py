import os
import shutil
"""
os module helps to interact with os function 
like , create folder, remove folder, get working directory
create path, check file and folder. 
"""

# Get current working directory

cur_dir = os.getcwd()
print(cur_dir)

# Get list of all file and folder in given path

tar_path = "C:\\Testdata"
data_list = os.listdir(tar_path)
print(data_list)

print(len(data_list))


# Create folder in current dir

#os.mkdir("C:\\Testdata\\tag_folder")

#create folder in curent directory
#os.mkdir('folder1')

"""
str1 = '1'
print(os.getenv("E:\\15feb2021\\venv"))
"""

# run windows commands

#os.system('control')
#os.system('appwiz.cpl')
#os.system('notepad.exe')

#####################################
# join two path

path1 = "C:\\testdata"
path2 = "folder2"

print(os.path.join(path1, path2))

filepath = "C:\\Testdata\\count_name.txt"

print(os.path.isdir(filepath))
print(os.path.isfile(filepath))

# copy file from one location to another

shutil.copy(filepath, "E:\\Filesdata\\file1.txt")