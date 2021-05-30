dict1={'k1':'M','k2':'U','k3':'P','K4':'Y','K5':'Z'}

#get asci value of char
dict2 = {}
for k, v in dict1.items():
    print(k, v, ord(v))
    dict2[k] = ord(v)

print(dict2)

# str1 = 'hello'
# print(dir(str1))
#
# for i in range(65, 91):
#     print(i, chr(i))