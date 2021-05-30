"""
The context has in build enter and exit function
with open(filename, mode) as fileobj:
    data = filobj.read()
    print(data)

"""
filename = 'context_manage.txt'
""""
with open(filename, 'r') as file:
    data = file.read()
    print(data)
"""

# tell() : gives current position of cursor in the file
# seek() : set cursor on different location and read data from there
         # seek helps to jump of character before reading the content.

"""
with open(filename, 'r') as file:
    print("beginning position :", file.tell())
    line = file.readline()
    print(line)
    print("position after reading one line :", file.tell())

    # set cursor on 100 char movement from beginning
    file.seek(100)
    # read line after 100 char movement
    print("100 char movement from beginning :", file.tell())
    # Read line after 100 char movement
    line2 = file.readline()
    print("line2 :", line2)
    #
    print("position after 100char movement, read line  :", file.tell())

    #set cursor at 200 char movement from beginning
    file.seek(200, 0)
    print("position after 200 char movement:", file.tell())
    line3 = file.readline()
    print("Line 3:", line3)
    print("position 200 char move and readline :", file.tell())

"""
################################
# Read all email from the file and add to the list.

#1 open file with context manager.
#2 read all lines using alllines method
#3 iterate through each line one by one using loop
#4 take word list from line using split method
#5 iterate through each word in wordlist using loop.
#6 check @ available in each word and consider it as email and add to email_list

#1 open file with context manager

email_list = []
with open(filename, 'r') as file:
    #2 real all lines
    alllines = file.readlines()

    #3 iterate through each line
    for line in alllines:

        # 4 get word list using split method
        word_list = line.split()
        #print(word_list)

        #5 Iterate through each word in wordlist
        for word in word_list:

            #6 check if @ available in the word
            if '@' in word and ('.com' in word or '.co.in' in word):
                email_list.append(word)
            else:
                continue


print(email_list)

