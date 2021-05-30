"""
 ***
*   *
*   *
*   *
*   *
*   *
 ***

 *
 **
 ***
 ****
 ***
 **
 *
"""
#1. write a print * at 2,3,4 and space at 1st and 5th position.
#2. write code to print * at 1st and 5th position and space at 2,3,4 position
#    repeat same pattern 5 times
"""
for i in range(1, 6):
    if i ==2 or i == 3 or i == 4:
        print("*", end="")
    elif i == 1 or i == 5:
        print(" ", end="")
print("\n")
for i in range(1, 6):
    for j in range(1, 6):
        if j ==2 or j == 3 or j == 4:
            print(" ", end="")
        elif j ==1 or j == 5:
            print("*", end="")
    print("\n")
#print("\n")
for i in range(1, 6):
    if i ==2 or i == 3 or i == 4:
        print("*", end="")
    elif i == 1 or i == 5:
        print(" ", end="")

"""
"""
 *
 **
 ***
 ****
 ***
 **
 *
"""
"""
#1. write a code to print a increment star from 1 to 5
#2. write a code to print a decremented * pattern from 4 to 1
count = 1
for i in range(1, 6):  #i=1, i =2, i = 3
    for j in range(1, i): #j= 0, 1, j= 0, 1, 2 | j = 0, 1, 2, 3
        print(count, end=" ")
        count = count+1
    print("\n")
temp = 1
for i in range(4, 1, -1): # i = 4, i = 3 , i = 2,
    for j in range(1, i):     # j = 1, 2, 3 | j = 1, 2 | j =1
        print(temp, end=" ")
        temp = temp +1
    print("\n")
"""

str1 = "Python"
str_len = len(str1)
print(str_len)
temp = ''
#i = -1, -2, -3, -4, -5, -6

for i in range(-1, -str_len-1, -1):
    print(str1[i],":",  temp)
    temp = temp + str1[i]

print(temp)
