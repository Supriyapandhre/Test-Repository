"""
if condition:
    code
else:
    code


if condition:
    <code>
elif condition2:
    <code>
elif  condition3
    <code>
"""

num = 21

if num%2 == 0:
    print("Its Even Number")
else:
    print("Its Odd Number")

"""
> : greater than operator
< : less than operator
>= : greater than equal to operator
<= : less than equal to operator
== : equal to operator
!= : not equal operator

AND

TRUE and TRUE : TRUE
FALSE and TRUE : FALSE
TRUE and FALSE : FALSE
FALSE and FALSE : FALSE

OR

TRUE or TRUE : TRUE
TRUE or FALSE : TRUE
FALSE or FALSE : FALSE
FALSE or TRUE  : TRUE 
"""

a = 40
b = 50
c = 60

#find out bigger number among three

# if a > b and a> c :  #  FALSE and  FALSE
#     print("A is bigger number :", a)
# elif b >a and b > c: # TRUE and FALSE
#     print("B is bigger number :", b)
# elif c> a and c > b:  # TRUE and TRUE
#     print("C is bigger number :", c)


if a > b or a> c :  #  FALSE or  FALSE
    print("A is bigger number :", a)
elif b >a or b > c: # TRUE or FALSE
    print("B is bigger number :", b)
elif c> a or c > b:  # TRUE or TRUE
    print("C is bigger number :", c)


#1.take user salary and year of experience from user.
#-> if exp > 1 year : 10% increament in salary
#-> if emp < 1 year : 5% increment in salary