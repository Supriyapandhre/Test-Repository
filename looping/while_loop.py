
"""

Continue : when ever we hit with this continue ke, it start next iteration in the loop
Break :  Once hit with break, then it break loop iteration.

"""

for i in range(1, 20):
    #print(i)
    if i == 4 or i == 7 or i == 15:
        print("continue")
        continue
    elif i == 8:
        break
    print(i, ": ", i*i)


str1 = "Hello Good Morning, How are you, we are learning python"


expect_char = 'w'

for char in str1:
    if char == expect_char:
        print("We are breaking loop")
        break
    else:
        print(char, end=" ")
        continue


#################################
num = 1
table = 6

while num <= 10:
    #print(num)
    print(num, "*", table, ": ", num*table)
    num = num + 1


print("#"*50)
#Write a python program to reverse a number

num1 = 235
# output = 532

reverse = 0

# num1 = 235, temp=5, reverse = 0*10 + 5 : 5
# num1 = 23, temp =3, reverse = 5*10 + 3 : 53
# num1 = 2 , temp=2, reverse = 53*10 + 2 : 532

while num1 > 0:
    temp = num1%10 # 5, 3, 2
    reverse = reverse*10 + temp # 0*10 + 5 : 5, 5*10 + 3 : 53, 53*10 + 2 : 532
    num1 = num1//10 # 235//10 : 23, 23//10 : 2

print("reverse:", reverse)

#########################################

#Infinite loop
"""
num1 = 1

while True:
    print(num1)
    num1 = num1 +1
    if num1 == 20:
        break
"""

num2 = 1
list1 = []
while True:
    user_input = input("Please enter your number :")
    list1.append(user_input)
    if num2 == 5:
        break

    num2 = num2 + 1

print(list1)



































