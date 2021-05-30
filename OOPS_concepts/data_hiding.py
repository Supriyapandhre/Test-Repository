"""
Data hiding in python is to show the intention to hide the data, but actually we don't hide the data.
_  : (single underscore)
__ : (double underscore)

"""

class student:
    # Write class documentation
    """
    This class contains all information about the student, which includes name, phone, email,  address
    etc.
    """
    # class variables
    name = 'John'
    _age = 25   #(with single underscore as prefix)
    __phone = 6464645645  #(with double underscore as prefix)


    def __init__(self, school_name, address):
        self._school_name = school_name
        self.__address = address

    def _shows_student_address(self):
        print(f"Student address : {self.__address}")

    def __school_name(self):
        print("School Name :", self._school_name)


    def all_data_method(self):
        print("This method contains all the student data")


obj = student('International School', 'Mumbai')

#access data without underscore

print("Name :", obj.name)
obj.all_data_method()
# Access variable or data with single underscore (_)
# In single under score we don't show in suggestion those variable and methods which has (_) as prefix
# but we can access.

print("Age :", obj._age)
obj._shows_student_address()

# Access variable or method which has double under score as prefix in the name
# double under as prefix means more restriction on the data to access out side the class.
# obj._classname__variablename

print("Phone :", obj._student__phone)
obj._student__school_name()


##############################
#get all the method of the class

print(type(obj))
print(dir(obj))

str1 = 'hello'

print(type(str1))

print("#"*50)
# Use magic method to get class info

print("class name :", obj.__class__)
print("module name :", obj.__module__)
print("Get variables and method, ", obj.__dir__())
print("Get class documentation :", obj.__doc__)