

array = [2,4,6,8]
it = iter(array)
print(it.__next__())
print(it.__next__())
print(it.__next__())





def make_counter():
    count = 0
    def next():
        nonlocal count
        count += 1
        return count
    return next
    
ctr = make_counter() 
    
print(ctr())
print(ctr())
print(ctr())