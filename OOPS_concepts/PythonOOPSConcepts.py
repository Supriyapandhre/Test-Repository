"""
1. Class : class is blue print of the object which contains all properties and attribute of the object.
2. Object : object is instance of the class through which we can access class properties.
3. Inheritance
4. Polymorphism
5. Data Hiding and Abstraction
"""

class Car:

    # object method/instance method
    def car_name(self):
        print("BMW")

    # object method/instance method
    def car_prize(self):
        print("35 Lac")

# create a object of the class or instance of the class
"""
car_obj = Car()

car_obj.car_name()
car_obj.car_prize()
print("_"*50)
car_obj2 = Car()

car_obj2.car_name()
car_obj2.car_prize()
"""

###################################################
# Constructor : It helps to initilize the object of the class.   __init__()
# Default Constructor : default constructor call by default while creating the class object, when it does
#     not have any parameter.
# Parametize Constructor : we have to explicitly def __init__ method to create parametize constructor.


class student:

    # class variable
    school_name = 'International Convent School'

    # parametize constructor of the class
    def __init__(self, name, age):
        self.st_name = name  # instance variable
        self.st_age = age    # instance variable

    # instance method/ object method
    def show_name(self):
        print(f"Student Name : {self.st_name}")

    # instance method/ object method
    def show_age(self):
        print(f"Student Age : {self.st_age}")

    def show_school_name(self):
        print(f"My school Name :{student.school_name}")


"""
st_obj = student('John', 40)
st_obj.show_name()
st_obj.show_age()

print("#"*50)
st_obj = student('Tejas', 60)
st_obj.show_name()
st_obj.show_age()
st_obj.show_school_name()

print(st_obj.school_name)
print(student.school_name)

"""

# self : self is nothing but a object of the class itself, always the first parameter of the instance method.
# by default first parameter as object of the class will called along with method, when we tr to access
# via object.

obj_new = student('Harry', 40)

obj_new.show_name()

student.show_name(obj_new)