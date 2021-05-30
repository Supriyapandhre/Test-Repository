
str1 = 'Hello'
str2 = "Hello Morning"
str3 = """We are learning python language"""
"""
print(str1, str2, str3)

# String Formating
var1 = "Python"
var2 = 345
var3 = 2.6

str_format1 = "Hello, this is var1 :"+var1+", this is var2 :"+str(var2)+" and var3 :"+str(2.6)
print(str_format1)

str_format2 = "Hello, this is var1 :{}, this is var2 : {} and var3 : {}".format(var1, var2, var3)
print(str_format2)

str_format3 = f"Hello, this is var1 :{var1}, this is var2 : {var2} and var3 : {var3}"
print(str_format3)

"""
str11 = "We are learning Python"

print(dir(str11))

"""
capitalize', 'casefold', 
'center', 'count', 'encode', 'endswith', 'expandtabs', 
'find', 'format', 'format_map', 'index', 'isalnum', 
'isalpha', 'isascii', 'isdecimal', 'isdigit', 
'isidentifier', 'islower', 'isnumeric', 'isprintable',
 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 
 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix',
  'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 
  'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 
  'translate', 'upper', 'zfill']
"""
"""
# lower to  upper and upper to lower
stra = "Hello, Good Morning"
print(stra.swapcase())
#
new_str = ""
for char in stra:
    print(char)
    if char.isupper():
        new_str = new_str + char.lower()
    elif char.islower():
        new_str = new_str + char.upper()
    else:
        new_str = new_str + char
print(new_str)



# upper to lower

print(stra.upper())

# lower
print(stra.lower())

# strip : remove first and last space from the string

strb = " Morning "
print(strb)
print(strb.strip())

# split : split the string on the basis of delimeters

strc = "Hello Good Morning"
#print(list(strc))

output = strc.split(" ")
print(output)
print(type(output))
print(output[0], type(output[0]))

# get all words from the string
# print all word in reverse.
str11 = "split the string on the basis of delimeters"

word_list = str11.split(" ")
print(word_list)

for word in word_list:
    print(word," :", word[::-1])


# replace content in the string
str22 = "split the string on the basis of delimeters"

output = str22.replace("basis", "Python")
print(output)

# find the sub string is available in the string or not.
sub_str = 'on'
print(str22.find(sub_str))
print(str22[17:19])

#check the string is title or not

print(str22.istitle())
print(str22.title())

# check if there is any digit is available or not.
print("#"*50)
str44 = "Python 39"

for char in str44:
    print(char, ":", char.isdigit())

# get count of any character in the string.
print("#"*50)
str55 = "heck if there is any digit is available or not"

print(str55.count("i"))

# for char in str55:
#     print(char, ":", str55.count(char))


temp_str = ''
for char in str55:
    if char in temp_str:
        continue
    else:
        print("temp_str :",temp_str )
        print(char, ":", str55.count(char))
        temp_str = temp_str + char


##########################################################################
# program : get max length word from the string.

str55 = "heck if there is any digit is available or not  gsdfgjdfsgjsdfklg"
#output = 'available'
# 1. get wordlist using split method.
# 2. iterate each word and using loop
# 3. get length of each word len(word)
# 4. check condition which word has greater length.


word_list = str55.split(" ")
print(word_list)

max_len = 0
exp_word = ''

for word in word_list:
    word_len = len(word)
    print(word, ":", word_len)
    if word_len > max_len:
        max_len = word_len
        exp_word = word
        print("Max_len :", max_len)
        print("exp_word :", exp_word)
    else:
        continue

    print("###############")


print("Max length :", max_len)
print("Expected word:", exp_word)


"""

# Get min length word from the string.
str66 = "heck if there is any digit is available or not q gsdfgjdfsgjsdfklg"

# 1. get wordlist using split method.
# 2. iterate each word and using loop
# 3. get length of each word len(word)
# 4. check condition which word has mini length.

word_list = str66.split(" ")
min_len = len(word_list[0])
exp_word = ''
print(min_len)

for word in word_list:
    word_len = len(word)
    print(word, word_len)
    if word_len <= min_len:
        min_len = word_len
        exp_word = word

    else:
        continue

print("min_len:", min_len)
print("Expected word :", exp_word)


###################################
# Program : most symultaneously repeated character in the string.
str77 = "sssdadfasdfa ggggg ffffffffffff"

#1. get each character one by one : apply loop on string
#2. check current char and next char if both are same.
print("#"*50)
char_count = 1
exp_char = ''
max_char_len = 1
for i in range(len(str77)-1):
    #print(str77[i])  # i = 0, s
    print("char_count :", char_count)
    print("char:", str77[i])
    print("max_char_len :",max_char_len)
    print("exp_char :", exp_char)
    if str77[i] == str77[i+1]: # i =0, 1 , s, s
        char_count += 1
        if char_count > max_char_len:
            max_char_len = char_count
            exp_char = str77[i]
    else:
        char_count = 1

    print("#"*50)

print(char_count)

print(max_char_len,":", exp_char)






















