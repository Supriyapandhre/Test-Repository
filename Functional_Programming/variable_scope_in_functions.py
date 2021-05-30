"""
Local variable : scope of local variable is inside of the function only
Global variable : scope of global variable is across the module , any function can use it.
non local variable : non local variables ct as global variable for inner function
"""
"""
# global variable
var1 = 60

def function1():
    print("we are in function1")
    var2 = 80 # local variable
    print("var1 global:", var1)
    print("var2 :", var2)

def function2():
    print("we are in function2")
    var3 = 100
    global var1
    var1 = 200
    print("var3 :", var3)
    print("var1 global:", var1)
    #print("var2", var2) we can not call other function local variable

def function3():
    print("we are in function3")
    var4 = 90
    print("var4 :", var4)
    print("var1 global:", var1)


print("#"*50)
function1()
print("#"*50)
function2()
print("#"*50)
function3()

"""
# global
x = 50

def outer_function():
    y = 60 # non local function
    # for outer function y is local variable
    # for inner function y is non local variable

    def inner_function1():
        print("we are in inner function1")
        z = 80 # local variable
        print("x global :", x)
        print("y non local:", y)
        print("z local :", z)

    def inner_function2():
        print("we are in inner function2")
        p = 80  # local variable
        nonlocal y
        y = 500
        print("x global :", x)
        print("y non local:", y)
        print("p local :", p)

    def inner_function3():
        print("we are in inner function3")
        q = 100  # local variable
        print("x global :", x)
        print("y non local :", y)
        print("q local :", q)

    inner_function1()
    print("#"*50)
    inner_function2()
    print("#" * 50)
    inner_function3()
    print("#" * 50)

# def outer_function2():
#     print("y :", y)

outer_function()










