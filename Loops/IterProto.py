class CustomRange:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        else:
            self.start = self.start + 1
            return self.start - 1

print("----------------------------------------")
c = CustomRange(1,4)
print(c.__next__())
print(c.__next__())
print(c.__next__())
#print(c.__next__())
#StopIteration as there are no items

print("----------------------------------------")
c1 = CustomRange(1,10)
print(list(c1))

print("----------------------------------------")
c2 = CustomRange(1,15)
for i in c2:
    print(i)
