import time as t
import itertools

def greet(fx):
    def mfx():
        print("Hi this is starting of decoratoer.")
        fx()
        print("This is end of decoratter.")
    return mfx


def calExecTime(fx):
    #et = st = 0.0
    def delta():
        st = t.time()
        fx()
        et = t.time()
        print("Execution time (in seconds) for the funstion is: ", et - st)
    return delta
   

@calExecTime
@greet
def hello():
    print("Hi there.")




hello()
