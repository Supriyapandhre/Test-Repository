#default value to the parameter
# default value parameter should always on right side
def function1(num1, num2, num3=80):
    print("Num1 :", num1)
    print("Num2 :", num2)
    print("Num3 :", num3)

    #print("Addition :", num1+num2)

# this value will refer num1 only and num2 will consider default value.
#function1(50)

# if we provide for default parameter then it will overwrite default so 6o will overwrite 30.
#function1(50, 60)

# function1(num2=70, num3=100, num1=80)
# function1(70, 100, num3=200)
#function1(70, 200, num2=100)
#function1([4, 7, 8], {'a':123}, 'Hello')

###############################################
# *args  : *args enable function to get any number of arguments

def function2(*args, num1=40):
    print("Num1 :", num1)
    print(args)
    for var in args:
        print(var)

def function3(*sqa, num1=40):
    print("Num1 :", num1)
    print(sqa)
    for var in sqa:
        print(var)

#function2(4, 6, 8, 'a', [4, 6, 7, 8], {'name':'rahul'}, (5, 7, 8), num1=50)
#function3(5, 6, 7, 8, 3)

# **kwargs : it helps to accept the arguments in the key value format.

def function4(**kwargs):
    print(kwargs)

    for k, v in kwargs.items():
        print(k, ":", v)

    db_user = 'rahul123'
    db_pass = 'admin@123'

    if 'username' in kwargs and 'password' and kwargs:
        if db_user == kwargs['username'] and db_pass == kwargs['password']:
            print("Login Successful")
        else:
            print("Invalid credentials")

    else:
        print("Required inputs are not available")


#function4(name='rahul', age=25, salary=50000, email='rahul@gamil.com', password='admin@1235')

# return : it enables function to return back the output

def function5(num1, num2):
    multi = num1*num2
    #print(multi)
    return multi
    #print("Write after return") # we can not execute anything after return statement

def addition(x, y):
    return x+y


var = function5(5, 4)
print(var)

print(addition(var, 60))


















