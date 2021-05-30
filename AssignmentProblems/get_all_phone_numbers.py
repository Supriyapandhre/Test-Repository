# 5. Write a python to get all phone number from the file.
# Condition: phone number should contain 10 digits.


#1 -> Get all lines from the file : file.readlines
#2 -> Go through each line using loop
#3 -> Get word list from each line using split method.
#4 -> Go through each word using loop
#5 -> Check word length should be 10 and word should contains on digit.
#6 -> if condition is true then append in phone_list

phone_list = []

#1 -> Get all lines from the file : file.readlines
with open("phone_directory", 'r') as file:
    all_lines = file.readlines()

    # 2 -> Go through each line using loop
    for line in all_lines:
        # 3 -> Get word list from each line using split method.
        word_list = line.split()
        # 4 -> Go through each word using loop
        for word in word_list:
            if len(word) == 10 and word.isdigit():
                # 6 -> if condition is true then append in phone_list
                phone_list.append(word)
            else:
                continue

print("Phone List:", phone_list)


