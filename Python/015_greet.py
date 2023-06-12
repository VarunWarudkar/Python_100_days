import time as t

def calExecTime(fx):
    #et = st = 0.0
    def delta():
        st = t.time()
        fx()
        et = t.time()
        print("Execution time (in seconds) for the funstion is: ", et - st)
    return delta

@calExecTime
def greet():
    currentTime = t.asctime()
    print()
    if int(currentTime[11:13]) < 12:
        print("Good Morning")
    elif int(currentTime[11:13]) == 12:
        print("Good Noon")
    elif int(currentTime[11:13]) > 12 and int(currentTime[11:13]) < 16:
        print("Good AfterNoon")
    elif int(currentTime[11:13]) > 16 and int(currentTime[11:13]) <= 23:
        print("Good Evening")

@calExecTime
def greet1():
    hr = int(t.strftime("%H"))
    if hr < 12:
        print("Good Morning")
    elif hr == 12:
        print("Good Noon")
    elif hr > 12 and hr < 16:
        print("Good AfterNoon")
    elif hr > 16 and hr <= 23:
        print("Good Evening")

print("current time is: ", t.asctime())
print("Invoking greet")
greet()

print("Invoking greet1")
greet1()
