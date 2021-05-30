"""
Polymorphism:
Overriding : Two class which in parent and child relation and both class contains same method name
then this concepts is known as method overriding.
and Prefrence will be given to that method , whose class object is being created.

Method Overloading : Same class contains two method with same name, with different behavior , then this concept
is known as method overloading.

Note : Python does not support method overloading, because the python is dynamic language
we don't defined what kind of data to be passed to the method,
-> if we define two method with same name, in the class, then it always always consider the
latest defined method not the previous one.

"""

class ABC:
    def __init__(self, name, surname):
        self.name= name
        self.surname  = surname

    def show_details(self):
        print("Name :", self.name)
        print("Surname :", self.surname)

    def show_msg(self):
        print("We are in class ABC")


class XYZ(ABC):

    def __init__(self, age, salary, name, surname):
        super().__init__(name, surname)
        self.age = age
        self.salary = salary

    def show_details(self):
        print("Age :",self.age)
        print("Salary :", self.salary)

    def addition(self):
        str1 = "Hello"
        str2 = "Monring"
        print(str1+str2)

    def addition(self):
        num1 = 50
        num2 = 60
        print(num1+num2)



obj = XYZ(25, 5000, 'Rahul', 'Gupta')

obj.show_details()
obj.show_msg()

# latest defined method will be called.
obj.addition()


