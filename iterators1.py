
class MyIterator:
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.curent=start
    def __iter__(self):
        return self

    def __next__(self):
        if self.curent>=self.end:
            raise StopIteration
        self.curent+=1
        return self.curent-1

iter = MyIterator(1,5)
for value in iter:
    print(value)