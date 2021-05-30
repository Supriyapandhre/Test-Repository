# lambda arguments:code expression


result = lambda x, y: x +y
print(result(60, 50))

result2 = lambda x, y: (x +y)*2
print(result2(60, 50))


result3 = lambda x, y: x if x%2 == 0 else y
print(result3(21, 30))


# Map :

def square(n):
    return n**2
list1 = [5, 7, 3, 8, 9]

output = list(map(square, list1))
print(output)

output2 = list(map(lambda x:x//2, list1))
print(output2)
