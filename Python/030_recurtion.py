

def factorial(n):
    '''calculate the factorial of given number. Function  takes only one argument and uses recurtion to calculate.'''
    if n < 0:
        print(f"privided input value {n} is invalid.")
        return -1
    elif n == 0  or n == 1:
        return 1
    else:
        return  n * factorial(n-1)

def fibonacciSequence(n):
    '''Calculate the fibonacci sequence of given number. Function  takes only one argument and uses recurtion to calculate.''' 
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciSequence(n -1) + fibonacciSequence(n-2)
    
doc1 = factorial.__doc__
doc2 = fibonacciSequence.__doc__
n = int(input("Please enter valid positive integer: "))
print(doc1)
m = factorial(n)
if m >= 0: 
    print(f"fatorial of {n} is: {m}")
else:
    print("error")

print(doc2)
l = fibonacciSequence(n)
if l >= 0: 
    print(f"fatorial of {n} is: {l}")
else:
    print("error")