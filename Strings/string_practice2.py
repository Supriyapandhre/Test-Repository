
""""
str1 ="Python"

# 1
print(str1[::-1])

# 2
output = reversed(str1)
print(output)

str2 = ''
for data in output:
    print(data)
    str2 = str2 + data

print(str2)

# 3
new_str = ''
for i in range(-1, -len(str1)-1, -1):
    print(i)
    new_str = new_str + str1[i]
print(new_str)

print("#"*50)
print(len(str1))

for i in range(-1, -len(str1)-1, -1):
    print(i, str1[i])


# range (start, end, difference) : it always skip the end value

str1 = "Python"
print("length :", len(str1))

for i in range(0, 5, 1):
    print(i)

for j in range(-1, -len(str1)-1, -1):
    print(j, str1[j])


"""

#######################################
# replace : replace content in given string.

str1 = 'Its string training session, learning is fun'

"""
output = str1.replace('session', 'classes')
print(output)

str1 = str1.replace('session', 'classes')
print(str1)

# 1. replace fourth index value with another one.
# 2. replace fourth index value which is s with  another char

str1 = 'Its String training session, learning is fun'
print(str1)
new_str = ''
new_char = 'T'

# condition 1: check specific index and replace the character
for i in range(len(str1)):
    if i == 4:
        new_str = new_str + "T"
    else:
        new_str = new_str + str1[i]
        print("New String: ", new_str)

# condition 2 : check specific index and character and replace it.
for i in range(len(str1)):
    if i == 4 and str1[i] == 'S' :
        new_str = new_str + "T"
    else:
        new_str = new_str + str1[i]
        print("New String: ", new_str)


print(new_str)

"""
# find char and substring in the string.

str22 = "find char and substring in the string."

print(str22.find('in'))


output = True if 'a' in str22 else False
print(output)


##########################
#1. Assignment

# 1. create a new string with all odd places character.
# str1 = "find char and substring in the string."

#2. replace 'and' with 'or' and change the case of each character.

#3. check specific substring is available in the string and get count of it.

# 9). Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).







