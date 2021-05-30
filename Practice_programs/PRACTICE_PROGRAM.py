"""
3. get 'python' as string and return dict like below output.
#dict = {'p' : '###p###', 'y': '__y__', 't': '++t++', 'h': '??h??', 'o':'==0==', 'n':'**n**'}

"""

str1 = 'python'
dict1 = {}

for char in str1:
    if char == 'p':
        dict1[char] = f"###{char}###"
    elif char == 'y':
        dict1[char] = f"__{char}__"

print(dict1)