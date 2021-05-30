#Program: read last three lines of file.
'''
fileobj = open('test1.txt', 'r')
alllines = fileobj.readlines()
print(alllines)
for i in range(-3, 0, 1):
    print(alllines[i])
'''





#Programs: replace all the SQATools with PYTHON

#1. read all lines from the file. readlines()
#2. go through line in list of lines. using loop
#3. Check if SQATools in available in the line through if condition
#4. if SQATools is available then replace with PYTHON and store in another resultlist.
    #-> if SQATools is not available in the line, then append that line to resultlist.

#5. create a string with resultlist using loop
#6. newly created string write to the file again.
src_string = 'JAVA'
tar_string = 'Zafar'

fileobj = open('test1.txt', 'r')

result_list = []
#step1
all_lines = fileobj.readlines()

#step2
for line in all_lines:
    #step3
    if src_string in line:
        # step4
        result = line.replace(src_string, tar_string)
        result_list.append(result)
    else:
        result_list.append(line)
fileobj.close()
print(result_list)

#step 5
new_str = ''
for line in result_list:
    new_str = new_str + line

#step 6
file2 = open('test1.txt', 'w')
file2.write(new_str)
file2.close()








