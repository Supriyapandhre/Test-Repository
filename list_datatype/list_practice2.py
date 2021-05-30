# List  comprehension
"""
# print square of all odd number
list1 = [5, 8, 3, 6, 7, 11, 13]

for i in list1:
    if i%2 != 0:
        print(i**2, end=" ")
    else:
        continue


# syntax [x for x in list1]

print("\n")
result = [x**2 for x in list1]
print(result)

result2 = [x**2 for x in list1 if x%2 != 0]

print("\n")
print(result2)



"""

########################################
# Programs
"""
list1 = [3, 5, 6, 8]
list2 = [6, 7, 8, 3, 2, 6]

#output = [(3, 6), (5, 7), (6, 8), (8, 3), 2, 6]

# 1. read list1 and list2 elements by index via loop.
# 2. combine same index element ans store inside of output
# 3. if list2 index is not available in list1, then store it separately

output = []
for i in range(len(list2)):
    if len(list1) > i:
        output.append((list1[i], list2[i]))
    else:
        output.append(list2[i])

    print(i, output)

print(output)
"""

################################################
#program :

str1 = 'Python'
#output = [('P', 'pPpP'), ('y', 'yYyY'), ('t', 'tTtT'), ('h', 'hHhH'), ('o', 'oOoO'), ('n', 'nNnN')]

#1. Get each char using loop
#2. create string with char and their lower and upper case case combination.
#3. Append char and its char combination in the output list.
output = []
for char in str1:
    temp = f"{char.lower()}{char.upper()}{char.lower()}{char.upper()}"
    combination = (char, temp)
    output.append(combination)

print(output)
































