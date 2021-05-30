"""
Three More Assignment Programs

1. Consider a list as input and create required dictionary
list1 = [5, 6, 7, 8, 9]
output = {5: 125, 6: 216, 7: 343, 8: 512, 9: 9**3}

2. get input string and print desired dictionary
str1 = "We are learning Python"
output = {'w' :'ew, 'a': ere, 'l':'gninrael', 'P': 'nohtyP'}

3. read all dictionary values store in three seprate list for odd, even, str.
dict1 = {'k1' : 23, 'k2': 14, 'k3': 25, 'k4': 56, k5: 'Hello', k6:'morning'}
output:
list1 = [23, 25]
list2 = [14, 56]
list3 = ['Hello', 'morning']

"""
"""
#1. Consider a list as input and create required dictionary
list1 = [5, 6, 7, 8, 9]
#output = {5: 125, 6: 216, 7: 343, 8: 512, 9: 729}

#1. Get each element from the list using loop.
#2. set list data as key and cube of that data as value

output = {}

for var in list1:
    print(var, ":", var**3)
    output[var] = var**3

print("Output :", output)

"""



"""

#2. get input string and print desired dictionary
str1 = "We are learning Python"
#output = {'w' :'ew, 'a': ere, 'l':'gninrael', 'P': 'nohtyP'}

#1. Get word list, using split method.
#2. Get each word from word list, using loop
#3. Get first char of each word, word[0]
#4. Get reverse of given word, word[::-1]
#5. store in dict first char as key and reverse of word as value

word_list = str1.split()
print(word_list)
result = {}

for word in word_list:
    print(word)
    first_char = word[0]
    print(first_char)
    reverse_word = word[::-1]
    print(reverse_word)
    result[first_char]  = reverse_word


print("Result :", result)

"""


#3. read all dictionary values store in three seprate list for odd, even, str.
dict1 = {'k1' : 23, 'k2': 14, 'k3': 25, 'k4': 56, 'k5': 'Hello', 'k6':'morning'}
"""
output:
list1 = [23, 25]
list2 = [14, 56]
list3 = ['Hello', 'morning']
"""
"""
#1. Get each key and value from the dict using: dict1.items()
#2. Check particular value is even then store in evenlist.  value%2==0
#3. check particular value is odd then store in odd list
#4. check particular value is str then store in string list

odd_list = []
even_list = []
string_list = []


for k, v in dict1.items():
    print(k, ":", v)
    if str(v).isdigit():
        if v%2 == 0:
            even_list.append(v)
        else:
            odd_list.append(v)
    else:
        string_list.append(v)

print("Odd list:", odd_list)
print("Even list:", even_list)
print("String list:", string_list)

"""
# Write a python program to sort by accending and decensing by value.

dict1 = {'a': 4, 'b': 7, 'c': 45, 'd' : 23}

#1. Get all key value combination using dict.items()
#2. Get max value from all the combination.
#3. append that max value tuple in result list.
#4. remove from output list result

# step1
result = dict1.items()
print(result)
lo = list(result)

#lo1 = lo.copy()
print(lo)
# [('a', 4), ('b', 7), ('c', 45), ('d', 23)]
result_list = []
lo_len = len(lo)
#steps2
for i in range(lo_len):
    print(lo)
    max = lo[0][1]  # max = 4
    desire = lo[0]  # ('a', 4)

    for element in lo: # ('a', 4), ('b', 7), ('c', 45), ('d', 23)
        if element[1] > max:
            max = element[1]  # max = 4, 7, 45
            desire = element  # desire = ('a', 4), ('b', 7), ('c', 45)
        else:
            continue
    result_list.append(desire)
    lo.remove(desire)
    print(max, desire)
    print("#"*50)

print(result_list)

print(dict(result_list))

dict3 = {}
dict1 = {'a' : 56, 'b' : 67}
dict2 = {'a': 500, 'c' : 65, 'd' : 34}

dict3['a'] = dict1['a']
dict3['c'] = dict2['c']

print(dict1.update(dict2))
print(dict1)

print(dict3)




















