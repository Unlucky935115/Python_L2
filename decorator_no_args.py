import time

def my_decorator(func):
    def wrapper():
        t1=time.time()
        print("Function execution start time: {}".format(t1))
        func()
        t2=time.time()
        print("Function execution end time: {}".format(t2))
        t3=t2-t1
        print("Function Execution time: {}".format(t3))
    return wrapper

print("=="*30)
@my_decorator
def hello_world():
    print("Hello World!!!")
hello_world()


print("=="*30)

def say_my_name():
    print("This is Unlucky's Coding")
my_fun=my_decorator(say_my_name)
my_fun()
print("=="*30)