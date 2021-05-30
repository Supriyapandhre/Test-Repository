"""
1. Number
      -> Integer
      -> Float
2. Sequence
     1. String
     2. List
     3. Tuple
3. Dictionary
4. Set
5. Boolean

"""

############################## List ##############################

#list1 = [3, 6, 7, 'hello', 'a', [4, 6, 3]]

"""
-> We can store any type of data in the list
-> List is a mutable data type, it means we can modify it when ever required
-> List follows indexing similar like string.
         0  1  2  3
list1 = [4, 6, 7, 8]
        -4  -3 -2 -1
"""

list1 = [3, 6, 7, 'hello', 'a', [4, 6, 3]]

print(type(list1))

print(list1[0])

output = list1[-1]

print(output[0])

out2 = list1[3]
print("output:", out2)

print(out2[1])

###### slicing ######
print(list1[2: 5])

print(dir(list1))

"""
List Method
append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""

list2 = [4, 6, 8]

list2.append(10)
print(list2)

#################################### Tuple ##############################
print("#"*50)
#tuple1 = ()
"""
-> Tuple is immutable data type , once data is defined we can not change it.
-> Tuple follows same indexing like list and string.
         0  1   2  3
tupe1 = (4, 6, 8, 7)
        -4 -3 -2 -1
"""

tupl1 = (4, 2.4, [3, 5, 6], (4, 5, 2), 'Good', 'a')

print(tupl1[0])

print(tupl1[-1])

# print list from tuple
print(tupl1[2])

# print list value from tuple
print(tupl1[2][0])

# print tuple from the tuple
print(tupl1[3])

# print child tuple value from outer tuple
print(tupl1[3][1])

# Method in tuple
print(dir(tupl1))
"""
These are the method available in the tuple
count', 'index'
"""

################################# Dictionary #####################

"""
dict1 = {key: value}
-> dict store data in the form key value pair
-> dict key are alwaqys unique, we can not store duplicate key in the dict.
-> dict is unstructure data type
-> dict is mutable data type , it means we can change the data at point of time
-> Only immutable data type can be key in the dictionary, e.g  tuple, string, integer
-> Any type of data can value in the dictionary e.g. int, float, string, list, tuple, dict
-> Dict does not follow any indexing

"""

print("#"*50)
dict1 = {'name': 'John', (4, 6, 7): 333, 'a' : 'morning', 'x': [4, 6, 7]}

print(dict1['name'])

print(dict1)

print(dict1['x'])

# get list value from the dict
output = dict1['x']
print(output[2])

# add new data to the dictionary
dict1['surname'] = 'Harry'

print(dict1)

dict1['name'] = 'Tejas'
print(dict1)


# Key all keys
keys = dict1.keys()
values = dict1.values()

print("keys: ", keys)
print("values :", values)

# Methods in the dictionary
print(dir(dict1))
"""
clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
"""

# we can not define list as key

#dict1[[4, 6, 7]] = 'Python'

"""
Thia error will be shown on your machine

dict1[[4, 6, 7]] = 'Python'
output: hello
TypeError: unhashable type: 'list'

"""


######################################## Set #######################################
print("#"*50)

"""
set1= {}
-> set is mutable data type, means we can modify it at any point of time
-> set does not follow any indexing
-> set only store unique values
-> We can not add list and dictionary inside the the set
-> set is a un structure data type

"""

set1 = {4, 7, 8, 3, 4, 7, 9, 'a', 'python', 2.5}
print(set1)

set1.add(10)
print(set1)

# We can not add list inside of set
#set1.add([4, 6, 8])
#print(set1)

"""
set1.add([4, 6, 8])
TypeError: unhashable type: 'list'
"""

# We can not add dict in the set

#set1.add({'a': 234, 'b':456})
#print(set1)

"""
set1.add({'a': 234, 'b':456})
TypeError: unhashable type: 'dict'

"""

# Methods available in the set
print(dir(set1))

"""
Method available in the set
'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
"""

list1 = [5, 7, 9, 23, 5, 6, 4, 5, 7]
print(set(list1))


############################ Boolean ##############
"""
True
False
"""

a = 50
b = 60
print(a > b)

print(a < b)




