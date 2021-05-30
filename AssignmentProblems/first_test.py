"""
1. Write a python script to parce the string and get all the employee id
from given string.

Input_str = "There are four employee with id emp_02 emp_405 emp_501 emp_605"
output = ['emp_02', 'emp_405', 'emp_501', 'emp_605']


2. Write a python string to re-write the string as expected output.

input_str = "Its time to learn python programming"
output = "iTS TiME To LeaRN PYTHoN PRoGRaMMiNG"


3. Get all key and values from dictionary, covert all upper to lower.

dict1 = {'a': {'name': 'Rahul'},
'b': [5, 6, 7, 8, (4, 6)],
567 : (5, 7, 6, 'Python')
}

4. Write a python program to read file and get all odd and even line in separate file
along with replace "Python" with "SQATools"

5. Write a python to get all phone number form the file.
Condition: phone number should contain 10 digits.

6. Write to Python to get longest word in the string and change it from upper to lower.

7. Write a python program Get last two max numbers in the the list.

list1 = [10, 50, 70 , 2, 45, 90, 22, 101]
output = [101, 90]
"""

#1. Write a python script to parce the string and get all the employee id
#from given string.
""""
Input_str = "There are four employee with id emp_02 emp_405 emp_501 emp_605"
#output = ['emp_02', 'emp_405', 'emp_501', 'emp_605']


list_word = Input_str.split()
output = []

for word in list_word:
    if "emp" == word.split("_")[0]:
        output.append(word)
    else:
        continue

print("Output :", output)
"""
"""
#2. Write a python string to re-write the string as expected output.

#input_str = "Its time to learn python programming"
#output = "iTS TiME To LeaRN PYTHoN PRoGRaMMiNG"

output = ''
vowel = 'aieou'

for char in input_str:
    if char in vowel:
        output = output + char
    else:
        output = output + char.upper()

print(output)

"""
"""

#3. Get all key and values from dictionary, covert all upper to lower.

dict1 = {'a': {'name': 'Rahul'},
'b': [5, 6, 7, 8, (4, 6)],
567 : (5, 7, 6, 'Python')
}
str1 = 'a'
print(type(str1))

for k, v in dict1.items():
    #print(k, ":", v)

    # Deal with keys, covert small to capital
    if str(type(k)) == "<class 'str'>":
        print(k.upper())
    else:
        continue

    # values
    if str(type(v)) == "<class 'dict'>":
        for k1, v1 in v.items():
            print(k1.upper(), v1.upper())

    elif str(type(v)) == "<class 'list'>":
        for data in v:
            print(data)
    elif str(type(v)) == "<class 'tuple'>":
        for data in v:
            print(data)
    else:
        continue

"""
"""
#4. Write a python program to read file and get all odd and even line in separate file
#along with replace "PYTHON" with "SQATOOLS"

#1. Get all lines of file
#2. go through each line using loop
#3. check index value of the line is odd or even
#4. Check PYTHON is available in the line or not
#5. If it is available then replace with SQATOOLS
#6. Add odd and even lines in two separate list
#7. Add those odd or even list in the two separate files.

odd_lines = []
even_lines = []

#1.  Get all lines of file
with open("testfile.txt", 'r') as file:
    alllines = file.readlines()

    # 2. go through each line using loop
    for i in range(len(alllines)):
        # 3. check index value of the line is odd or even
        if i%2 == 0:
            evenline = alllines[i]
            # 4. Check PYTHON is available in the line or not
            if "PYTHON" in evenline:
                # 5. If it is available then replace with SQATOOLS
                newlinse = evenline.replace("PYTHON", "SQATOOLS")
                # 6. Add odd and even lines in two separate list
                even_lines.append(newlinse)
            else:
                even_lines.append(evenline)

        else:
            oddline = alllines[i]
            if "PYTHON" in oddline:
                # 5. If it is available then replace with SQATOOLS
                newlinse = oddline.replace("PYTHON", "SQATOOLS")
                # 6. Add odd and even lines in two separate list
                odd_lines.append(newlinse)
            else:
                odd_lines.append(oddline)

print("Even List :", even_lines)
print("Odd List :", odd_lines)

#7. Add those odd or even list in the two separate files.

for line in even_lines:
    with open("evenlist_test.txt", "a") as file:
        file.write(line)


for line in odd_lines:
    with open("oddlist_test.txt", "a") as file:
        file.write(line)
"""
#####################################################################






























