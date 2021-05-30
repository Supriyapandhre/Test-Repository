class A:
    def method1(self):
        print("We are in class A and Method1")

    def method2(self):
        print("We are in class A and Method2")

# create a object
obj1 = A()
obj1.method1()
obj1.method2()

############################################

class B:

    # constructor of the class
    def __init__(sqa, name, age):
        sqa.name = name
        sqa.age = age

    def show_name(sqa):
        print("Name :", sqa.name)

    def shows_age(sqa):
        print("Age :",sqa.age)


obj2 = B('John', 56)

obj2.show_name()
obj2.shows_age()


obj3 = B('Harry', 25)

obj3.show_name()
obj3.shows_age()

# self : self refer to same class object on which we are working.