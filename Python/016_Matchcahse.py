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
    hr = int(t.strftime("%H"))
    match hr:
        case 12:
            print("Good Noon")
        case _ if  hr < 12:
            print("Good Morning")
        case _ if  hr > 12 and hr < 16:
            print("Good AfterNoon")
        case _ if  hr > 16 and hr <= 23:
            print("Good Evening")

print("current time is: ", t.asctime())
greet()

for i in range(3, 31, 3):
    print(i)