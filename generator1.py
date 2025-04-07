def count_upto(max_value):
    count = 1
    while count <= max_value:
        yield count
        count += 1


count=count_upto(5)
try:
    print(next(count))
    print(next(count))
    print(next(count))
    print(next(count))
    print(next(count))
    print(next(count))
except StopIteration:
    print("Count Exceeded!!!")

