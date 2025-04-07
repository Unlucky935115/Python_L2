import time
from functools import wraps

def my_decorator1(func):
    @wraps(func)
    def wrapper1(*args,**kwargs):
        t1=time.time()
        print("This is decorator 1 and start time: {}".format(t1))
        result1=func(*args,**kwargs)
        t2=time.time()
        print("This is decorator 1 and end time: {}".format(t2))
        return result1
    return wrapper1

def my_decorator2(func):
    @wraps(func)
    def wrapper2(*args,**kwargs):
        t1 = time.time()
        print("This is decorator 2 and start time: {}".format(t1))
        result2 = func(*args, **kwargs)
        t2 = time.time()
        print("This is decorator 2 and end time: {}".format(t2))
        return result2
    return wrapper2

@my_decorator1 #decorator1 wraps the result of my_decorator2(hello_hi)
@my_decorator2 #decorator2 wraps the results of hello_hi function
def hello_hi(name):
    """
    This Function says hello hi
    """
    for i in range(10):
        print("{}) Hello Hi {}".format(i,name))
print("Function Name: ", hello_hi.__name__)
print("Function Description: ", hello_hi.__doc__)
hello_hi("Unlucky")
