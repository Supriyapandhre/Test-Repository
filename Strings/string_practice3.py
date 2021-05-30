#9). Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).
"""
line1 = 'djsdfksjafa J sdfasdf HJ dfdsH Good Mornirg'
line2 = 'Hello How are you'
line3 = 'We are learning Python Programsing'
line4 = 'Skilled persons are Required in The industry'

list2 = [line1, line2, '', line3, '', line4]

for line in list2:
    if line == '':
        continue
    else:
        print(line.lower())

"""
#Input_str1 = "sqa tools"
#Input_str2 = "python"

lines = []
while True:
    l = input("Please enter your string :")
    if l:
        lines.append(l.upper())
    else:
        break
for l in lines:
    print(l)

# Output :
#
# SQA TOOLS
# PYTHON
#
# """