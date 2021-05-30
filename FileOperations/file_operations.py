"""
file = open('file/filepath', 'mode')
r : read
w : write
a : append

read() : read complete file content in one go, and file cursor always start from beginning
readline() : it help to read one line at a time
readlines() : it all lines of file and return in the form list.
"""
"""
def read_file(filepath):
    filebj = open(filepath, 'r')
    data = filebj.read()
    print(data)
    # name
    print("name:", filebj.name)
    print("mode :", filebj.mode)

filepath = "E:\\15feb2021\\FileOperations\\sample.txt"
read_file("sample.txt")
print("#"*50)
read_file(filepath)

"""

# readline : this method read one line at a time.
def get_file_line(filename='sample.txt'):
    fileobj = open(filename, 'r')
    line = fileobj.readline()
    print(line)

#get_file_line(filename='sample.txt')



# readlines : this method read all lines in the form of list.
def get_file_all_lines(filename='sample.txt'):
    fileobj = open(filename, 'r')
    all_lines = fileobj.readlines()
    print(all_lines)
    # line 5
    print(all_lines[4])

#get_file_all_lines(filename='sample.txt')
"""
file1 = open('sample2.txt', 'r')
data = file1.read(10)
print(data)
line = file1.readline()
print(line)

"""
#######################################
# Write mode (w) : in this mode data write to the file will be overwrite.
# it specified file does not exist, then create new file and add content
def write_content_to_file(filename, str1):

    fileobj = open(filename, 'w')
    fileobj.write(str1)
    fileobj.close()

str1 = 'dfasdfasdf agfdgsdfgdfsg sdfgsdfggdfsgsdf'
write_content_to_file('demo2.txt', str1)

# append mode (a):
# -> Add data to the at the end, if file already exist add data at the end.
# -> If file does not exist, then create new one.

def append_data_to_file(filename, inputstr):
    fileobj = open(filename, 'a')
    fileobj.write(inputstr)
    fileobj.close()



inputstr = 'Add data to the at the end, if file already exist add data at the end.'
inputstr2 = '\n Python Learning is Fun'
#append_data_to_file('append_data_txt', inputstr)
append_data_to_file('append_data_txt', inputstr2)







