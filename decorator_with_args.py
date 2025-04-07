import time
def my_decorator(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        print("Function execution start time: {}".format(t1))
        result=func(*args,**kwargs)
        t2 = time.time()
        print("Function execution end time: {}".format(t2))
        t3 = t2 - t1
        print("Function Execution time: {}".format(t3))
        return result
    return wrapper

print("=="*30)
@my_decorator
def sample_fn(name):
    for i in range(10):
        print("{}) Hello {}".format(i, name))
sample_fn("Unlucky")
print("=="*30)
def unlucky_function(name):
    for i in range(10):
        print("{}) Hyii {}".format(i,name))
unluck=my_decorator(unlucky_function)
unluck("Unlucky")
print("=="*30)