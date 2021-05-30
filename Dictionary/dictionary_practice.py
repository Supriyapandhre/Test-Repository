# dict1 = {key : value}

"""
Properties
-> Dict is muttable data type we can change it when ever we want.
-> dict store the data in the form key value pair.
-> all immutable data type can be key in the dictionary, like string, integer, tuple, float
-> all other type of data type can be value in the dictionary e.g int, str, list, tuple, set, boolean.
-> all key by default unique in the the dictionary.
-> Dict is unstructured data type
"""

dict1 = {'a' : 123, 'b': 456, 5: 'Hello'}

# read data using key
print(dict1['a'])

# add data to the dictionary
dict1['c'] = 565
print(dict1)

#try to list as key in the dictionary : this operation is not allowed in dictionary
#list1 = [4, 5, 6]
#dict1[list1] = 'Hello Good Morning'


# add tuple as key

tup1 = (6, 7, 8)

dict1[tup1]  = [4, 7, 8, 9]
print(dict1)

output = dict1[tup1]
print(output[2])

# Get all keys from the dictionary

allkeys = dict1.keys()
allvalues = dict1.values()

print("Keys :", allkeys)
print("Values :", allvalues)

# ALl methods available in dictionary

print(dir(dict1))

"""
'clear', 'copy', 'fromkeys', 'get', 
'items', 'keys', 'pop', 'popitem', 
'setdefault', 'update', 'values']
"""
print("#"*50)
dict2 = {'p' : 'Hello', 'q': 'How', 'r': 'Are you'}
# Get method

output = dict2.get('q')
print(output)

# pop method : remove data from the dictionary
print("#"*50)
result = dict2.pop('q')
print("result :", result)
print(dict2)

# update method

dict11 = {'a': 456, 'b': 234, 'c': 121}
dct22 = {'x' : 'Spider', 'y': 'Jerms'}

dct22.update(dict11)
print("dict22 :", dct22)

#################################
#items
print("#"*50)
dictx = {'a': 456, 'b': 234, 'c': 121, 'd': 567}

print(dictx.items())

list1 = [5, 7, 8, 9]
list2 = ['A', 'B', 'C', 'D']

#print(dict(zip(list1, list2)))
zipdata = zip(list1, list2)
for data in zipdata:
    print(data)

#####################################
#Apply loop on dictionary
print("#"*50)
dicty = {'a': 456, 'b': 234, 'c': 121, 'd': 567}

for k, v in dicty.items():
    print(k, v)


for data in dicty:
    print(data)

# Check any particular key is available in dictionary or not.
input_key  = 'f'
if input_key in dicty:
    print(True)
else:
    print(False)

#########################################
# Programs
print("#"*50)
str1 = 'Python'
#output = {'P': 'ppp', 'y': 'yyy', 't': 'ttt', 'h':'hhh', 'o':'ooo', 'n': 'nnn'}
#1. read each character by loop in string.
#2  add inside that char as key and same three of char should be a value
output = {}
for char in str1:
    output[char] = char*3

print(output)


####################
# program :
# Maintain two dict with vowel and consonant, char should be key and their count should be value

str1 = "Maintain two dict with vowel and consonant, char should be key and their could should value"
vowel_dict = {}
consonant_dict = {}
vowels = 'aeiou'

#1. Get each char from string using loop
#2. Check that char is vowel or not
#3. get count of that char
#4. add inside of respective dict

for char in str1:
    if char in vowels:
        v_count = str1.count(char)
        vowel_dict[char]  = v_count
    else:
        c_count = str1.count(char)
        consonant_dict[char] = c_count

print("Vowel dict :", vowel_dict)
print("Consonant dict :", consonant_dict)


















#