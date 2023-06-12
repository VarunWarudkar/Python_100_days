def addition(*numbers):
    #print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum


c= addition( 1,2,3,4,7)
d = addition(1.2,4,7,8,9)

print(c)
print(d)