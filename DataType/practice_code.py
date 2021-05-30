list1 = ['a', 'Hello', 4.2, 'Zafar', 0]

print(list1[0:3])

print(list1[3][0:3])

list2 = []
list2.append(list1[3][0:3])
print(list2)

print(list1[0:3] + list2)

