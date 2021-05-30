
        #0  1  2   3
tuple1 = (3, 6, 8, 9, 'q', 'Hello', 2.5)
         #         -4  -3   -2       -1
# -> Tuple is immutable data type, we can not change the data in the tuple
# -> Tuple follows same indexing like string and list. e.g positive index and negative index.
# -> We are store any type of data in inside to the tuple.
# -> once tuple is defined , everything will remain constant, we can value like , days in week, months in years.

# positive index
print(tuple1[0])

# negative index
print(tuple1[-1])

# slicing
print(tuple1[2: 6])

# Method available in the tuple
print(dir(tuple1))
"""
'count', 'index'

"""
print("#"*50)

tup1 = (5, 6, 78, 23, 67, 5, 6)

# count

print("count of 5 :", tup1.count(5))

# get index

print("Index of 23: ", tup1.index(23))

# max value
print("max value :", max(tup1))
# min value

print("Min value :", min(tup1))
# sum all number

print("Sum of all number :", sum(tup1))




##############################################
# programs
print("#"*50)
tuple2 = (4, 5, 7, 8, 9)

fact_list = []

#1. interate through the tuple and get each element via loop
#2. Calculate factorial of each number
#3. append factorial to the list.


for num in tuple2:
    fact = 1
    for i in range(1, num+1):
        fact = fact*i
    fact_list.append((num, fact))

print(fact_list)







#num = 5 : 5*4*3*2*1

# num = 5
# fact = 1
#
# for i in range(1, num+1):
#     fact = fact*i
# print(fact)



















