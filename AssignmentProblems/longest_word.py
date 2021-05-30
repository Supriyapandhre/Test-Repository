#6. Write to Python to get longest word in the string and change it from upper to lower.

str1 = "Write to Python to get longest word in the GoodMorning and change it from upper to lower."
max_len =0
long_word = ''
#1 -> Get all word list from the string using split method.
#2 -> Go though each word and get the len of the word.
#3 -> compare word length with max_len, if word length if greater then set max_len=word_len
#     and set long_word = word
#4 -> Change upper to lower of the longest word.


#1 -> Get all word list from the string using split method.
word_list = str1.split()

#2 -> Go though each word and get the len of the word.
for word in word_list:
    word_len = len(word)
    if word_len > max_len:
        max_len = word_len
        long_word = word
    else:
        continue

print("Max Length: ", max_len)
print("Long word: ", long_word)

#4 -> Change upper to lower of the longest word.
print(long_word.swapcase())



