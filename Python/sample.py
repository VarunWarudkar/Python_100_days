import numpy

def arrays(arr):
    temp = [flaot(i,0) for i in  arr[::-1]]
    return temp

arr = input().strip().split(' ')
result = arrays(arr)
print(result)