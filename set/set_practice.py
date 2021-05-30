set1 = set()

"""
properties :

-> set in immutable datatype. we can add remove values from set.
-> set is unstructure data type, which does not follow any index.
-> Set contains only unique
-> We can all type of data inside except list and dictionary 
"""

set1 = {5, 7, 8, 2, 5, 6, 'a', 'Hello'}
print(set1)
print(type(set1))

# Methods is set.
print(dir(set1))

"""
'add', 'clear', 'copy', 
'difference', 'difference_update', 
'discard', 'intersection', 'intersection_update', 
'isdisjoint', 'issubset', 'issuperset', 
'pop', 'remove', 'symmetric_difference', 
'symmetric_difference_update', 'union', 'update']
"""

##################################################
print("#"*20)
set11 = {1, 56, 23, 78}

#add value to the set
set11.add(90)
print(set11)

#remove

set11.remove(23)
print(set11)

# pop :  this method remove element from set in random order and return back.

output = set11.pop()
print("output :", output)

# update

seta = {'a', 'b', 'c'}
setb = {3, 6, 8, 'a'}

seta.update(setb)
print("seta :", seta)

# union : get all unique elements from both the sets

seta = {'a', 'b', 'c', 'd'}
setb = {3, 6, 8, 'a'}

r_set = seta.union(setb)
print(r_set)
print("seta :", seta)
print("setb :", setb)

# difference : get difference values from one set to another.
print("#"*20)
setp = {'d', 'c', 'a', 'b', 6}
setq = {8, 3, 'a', 6}

print(setp.difference(setq))

# sysmmetric difference : get all unique value from both the sets, and avoid duplicate values.
print(setp.symmetric_difference(setq))

#####################################
# copy
print("#"*50)
# shallow copy
setp = {'d', 'c', 'a', 'b', 6}

setr = setp
setr.add(77)

print("setp :", setp)
print("setr :", setr)

# Deep copy
print("#"*50)
setx = {'d', 'c', 'a', 'b', 6}
sety = setx.copy()
sety.add(66)

print("setx:", setx)
print("sety:", sety)

###############################
#Check subset

setz = {'a', 'b', 66, 6, 'd', 'c'}
temp = {'a', 'b', 44}

print(temp.issubset(setz))


###################################
# Add different data in set

setp = {'g', 'h', 6, 7}
print(setp)

# add tuple to set

setp.add((6, 7, 8))
print("setp: ", setp)


# add list to set : adding list to set is not allowed
""""
list1 = [5, 2, 45, 34]
setp.add(list1)
"""
# add dict to set : adding dict to set is not allowed.

# setp.add({'name': 'john', 'age': 67})
# print(setp)

########################################################
print("#"*50)
# Get all unique value from list
list1 = [5, 7, 8, 3, 9, 2, 5, 3, 2, 3]
print(set(list1))

set2 = set()

for i in list1:
    set2.add(i)

print(list(set2))
















