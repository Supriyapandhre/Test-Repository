"""
When one operator perform multiple task then this is called operator overloading
like + , * etc
and behind the scene + operator is overloaded by "__add__" method.
and * operator is overloaded by "__mul__" method.

"""

num1 = 50
num2 = 60
print(num1+num2)


print(int.__add__(num1, num2))
print(str.__add__('Hello', 'Morning'))

print(int.__mul__(4, 5))
print(str.__mul__("#", 50))

print("#"*50)