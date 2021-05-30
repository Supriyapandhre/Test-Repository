    #    0  1  2  3   4    5
list1 = [5, 7, 8, 9, 'a', 'Hello']
    #   -6 -5 -4 -3  -2    -1

print(list1[0])

print(list1[-6])

# append : add data in the list at the end.

list1.append(30)
print(list1)

# insert : insert data at specific position or index
# list1.insert(index, value)
list1.insert(4, 50)
print(list1)

# remove : remove data from the list.

output3 = list1.remove(8)
print(list1)
print("output3", output3)

# pop : pop method remove data from specific index , default index is -1
print("#"*50)
list2 = [5, 6, 7, 8, 20]

# pop with default index , -1
output = list2.pop()
print("output", output)
print(list2)

# pop with specific index
output2 = list2.pop(3)
print(output2)
print(list2)

#############################
# program :
listx = [5, 7, 8, 9, 34]
listy = []
lenx = len(listx)
for var in range(lenx):
    temp = listx.pop()
    listy.append(temp)

print("Listx", listx)
print("Listy", listy)

#########################
# Add multiple element at a time
# extend : we can merge two list using extend

lista = [5, 8, 3, 4, 22]
listb = [6, 8, 23]

lista.extend(listb)

print("lista", lista)
print("listb", listb)

listp = [6, 8, 34, 4]
listq = [5, 22, 44, 66]

listr = listp + listq

print("listr", listr)
print("listp", listp)
print("listq", listq)

##############################
print("#"*50)
lists = [6, 5, 3, 2, 7, 5, 5]

#count
print("count 5:", lists.count(5))

#index
print("index of 2 :", lists.index(2))

#sum
print("sum :", sum(lists))

#max
print("max :", max(lists))

#min
print("min:", min(lists))

########################################















