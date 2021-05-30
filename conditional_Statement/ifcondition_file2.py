#1.take user salary and year of experience from user.
#-> if exp > 1 year : 10% increament in salary
#-> if emp < 1 year : 5% increment in salary

# salary = float(input("Please enter emp salary :"))
# exp = float(input("Please enter emp experiance :"))
#
# if exp > 2:
#     new_salary = salary + salary*10/100
#     print(new_salary)
# elif exp < 2:
#     new_salary = salary + salary*5/100
#     print(new_salary)
#

"""
list1 = [3, 6, 8, 9]
list2 = [6, 7, 8, 2]

output = zip(list1, list2)
print(output)

# for i in output:
#     print(i)

print(dict(output))
"""


import json
str2 = '{"name": "JOhn", "Age": 45, "Address": "Pune"}'

print(type(str2))

result = json.loads(str2)

print(type(result))

print(result['name'])


with open("data.json","r") as file:
    data = file.read()
    print(type(data))

    json_data = json.loads(data)
    print(type(json_data))