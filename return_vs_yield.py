import sys

def return_count_upto(max_value):
    return [i for i in range(1,max_value+1)]

def yield_count_upto(max_value):
    for i in range(1,max_value+1):
        yield i

max_value=10000

return_list=return_count_upto(max_value)
return_memory_usage=sys.getsizeof(return_list)

yield_list=yield_count_upto(max_value)
yield_memory_usage=sys.getsizeof(yield_list)

print("output when return statement is used: ")
print(return_list)
print("Memory usage when return used is: ",return_memory_usage," bytes")

print("output when yield statement is used: ")
print(next(yield_list))
print(next(yield_list))
print("Memory usage when yield used is: ",yield_memory_usage," bytes")
