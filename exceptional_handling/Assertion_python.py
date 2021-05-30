# Assertion help to verify the content and result as per expectation or not.

num1 = 10
num2 = 30



"""
if num1 == num2:
    print("Equal")
else:
    print("Not equal")
"""


# assert num1 == num2, "Checking number comparision"
#
# print("Operation Successful")

try:
    assert num1 == num2, "Checking number comparision"
    print("Operation Successful")
except Exception as e:
    print("Both number are not equal")
    #raise(e)


print("We are working on code module")