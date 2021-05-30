"""
def <function_name>:
    <code logic>

function()
#
-> Functions helps to manage the code properly.
-> Code written in function are code block, that can user any number times.
-> Function help to avoid duplicacy of code.
-> multiple function can intract with other each share their input and output.
   which helps us to increase efficiency
"""

def show_msg():
    print("Hello, We started learning functional programming")

# show_msg()
# show_msg()
# show_msg()

# pass parameter to the function
def show_msg2(msg):
    print("New Msg:", msg)


show_msg2('Good')
show_msg2('Morning')
show_msg2('Learning')

# functions parameters

def function1(num1, num2):
    print(num1+num2)

x = 40
y = 50
# pass by refrence
function1(x, y)

#pass by value
function1(60, 70)

function1('Hello ', 'Morning')

def employee(name, age, salary, email):
    print(f"Emp Name : {name}")
    print(f"Emp Age : {age}")
    print(f"Emp Salary : {salary}")
    print(f"Emp Email : {email}")


emp1= 'john'
age1= 45
salary1 = 78999
email1= 'john@test.com'

employee(emp1, age1, salary1, email1)
print("#"*50)

emp2= 'johnfds'
age2= 50
salary2 = 5555
email2= 'johndoe@test.com'

employee(emp2, age2, salary2, email2)


print("#"*50)
employee('sachin', 58, 100000, "sachine@gamil.com")
print("#"*50)
employee('sachin2', 70, 200000, "123sachine@gamil.com")
print("#"*50)
employee('Risabh', 25, 300000, "55sachine@gamil.com")