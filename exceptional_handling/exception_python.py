"""
Exception Handling : Exception handling help to customize error message and handle the exception in our own
way

try:
    <code>
except:
    <error handling code>

1. Divide by Zero  : ZeroDivisionError: division by zero
2. Name Error
3. Indedation error
4. IO Error

"""
"""
try:
    num1 = 30
    output = num1/12
    print(output)
    print("Division is Successful :", output)
    print("Intendation Error Fixed")

except:
        print("Number can not divide by zero")
 """

 # Try and Except with else
 # If there is no exception then execute else condition
"""
try:

    name = "Rahul"
    num1 = "567"
    print(name+num1)
except:
    print("Can not add, number and string")

else:
    # execute this code if there is not exception.
    print("Concatenation Success Full")
"""

# Catch a exception and print
# raise : raise helps us to fail the test cases explicitly and provide complete failures details
"""
try:

    name = "John"
    num1 = "567"
    print(name+num1)
except Exception as e:
    print("Can not add, number and string")
    print(e)
    raise(e)
"""


# Finally : The code block in this section will execute , even if there is exception in program or not.from

"""
try :
    username = input("PLease enter username :")
    password = input("PLease enter password :")

    db_user = 'Vipin'
    db_password = 'P@ssw0rd'

    if db_user == username and password == db_password:
        print("Login SuccessFull")
    else:
        raise("Invalid credential")
except Exception as e:
    print("Invalid credentials , we can not login")
    print(e)

finally:
    print("We are in home page")
"""

def factorial(num1):
    fact = 1
    for i in range(1, num1+1):
        fact=fact+i/0

    return fact


try:
    print(factorial(5))
except Exception as e:
    raise e

























