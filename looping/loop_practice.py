# print(1)
# print(2)
# print(3)
# print(4)
#print(5)

# range(start, end, difference)

#range(0, 5, 1)

"""
for i in range(0, 20, 2):
    print(i)
"""

"""
#if first and difference value is not set then default irst value is 0 and difference is 1
 
for j in range(10):
    print(j)
    
"""
"""
# print all ood and even
for j in range(50):
    if j%2 == 0:
        print("even :", j)
    else:
        print("Odd :", j)
 
"""
# print table of any number
"""
num = 3

for i in range(1, 11):
    print(i, "*", num ,": ",i*num)
"""
#######

# take 5 inputs from user and check they are divide by 5 and 7 or not.
# step 1 : take 5 inputs
# step 2 : check each number is divide by 5 and 7 or not

"""
list1 = []

for i in range(1, 6):
    str1 = "Please enter num "+str(i)+ ":"
    num = int(input(str1))
    list1.append(num)

print(list1)

for num in list1:
    if num%5 == 0 or num%7 == 0:
        print(num, ":",True)
    else:
        print(num, ":", False)
"""

"""
for i in range(1, 6):
    num = int(input("Please enter num"+str(i)+":"))
    if num%5 ==0 and num%7 == 0:
        print(num, "it can divide")
    else:
        print(num, 'it can not divide')

"""

#######################################
#Nested Loop condition
"""
for add in range(3): # i = 0, j = 0, 1, 2
    for parcel in range(5):
        print("address: ", add, "# parcel:", parcel)

    print("#"*50)
"""
# Get combination of all two number  there sum should be 10
        #v1
list1 = [5, 7, 8, 2, 6, 4, 9, 3, 1, 5]
        #v2, 5, 7, 8, 2, 4, 9, 3, 1
for var1 in list1:
    #print(var1)   var1 = 5, 7, 8
    for var2 in list1:
        # var2 = 5, 7, 8, 2, 6, 4, 9, 3, 1
        if var1 == var2:
            continue
        else:
            addition = var1 + var2
            print(("var1 :", var1,"|| var2 :", var2))
            if addition == 10:
                print(var1, var2)
            else:
                continue
    print("#"*50)





























