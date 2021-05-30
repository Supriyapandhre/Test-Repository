num1 = 50
print(type(num1))

# int to string

var= str(num1)
print(var)
print(type(var))

# float to string
num2 = 5.6

print(type(num2))
var2 = str(num2)
print(type(var2))

var3 = 'Hello'

print(var2+var3)
#print(num2 + var3)


print("#"*50)
# string to int
# -> if string contains only number then we can type as int.

str1 = '4576'
print(type(str1))

var4 = int(str1)
print(var4)
print(type(var4))


# list to tuple

list1 = [2, 5, 7, 8]
print(list1)
tup = tuple(list1)
print(tup)

print("###"*50)
# tuple to list
tup1 = (5, 7, 8, 3)
print(tup1)
list2 = list(tup1)
print(list2)

print("#"*50)

# string to list
str1 = "Hello Good"

list2 = list(str1)
print(list2)
tup1 = tuple(str1)
print(tup1)

# dictionary to str
print("#"*50)
dict1 = {'a': 34, 'b': 45}
print(type(dict1))
print(dict1['a'])

output2 = str(dict1)

print(output2)
print(type(output2))
print(output2[0: 5])

# we can not convert str to dict, it does not have key value pair.
print("#"*50)
#str2 = 'adfjadfjaskldfjasf'
#output3 = dict(str2)

import json
str3 = '{"a": 456, "b": 23, "c": 456}'

#output4 = dict(str3)
output4 = json.dumps(str3)

print(output4)
print(type(output4))

# dict to tuple : it will return only keys in the tuple
dict1 = {'a': 34, 'b': 56}
print(tuple(dict1))

list1 = [4, 7, 9]
list2 = [6, 8, 9]

var = zip(list1, list2)

print(dict(var))


# str to set
print("#")
set1 = {5, 7, 8, 4}
var = str(set1)
print(var, type(var))

str2 = "Hello Good Morning"

var2 = set(str2)
print(var2)

print(type(var2))

# set to tuple and tuple to set

set1 = {5, 7, 89, 3, 6}
tup = tuple(set1)
print(tup)

tup2 = (5, 7, 8, 23, 4, 5)
set2 = set(tup2)
print(set2)


# Set to dictionary and dictionary to set

print("#"*50)

set11 = {5, 7, 8, 9, 5}

# dict1 = dict(set1)
# print(dict1)

dict2 = {'a' : 678, 'name' : 'john', 'age': 35}
#list2 = list(dict2)
str2 = str(dict2)
print(list(str2))


