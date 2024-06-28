# Next
# next()
# give the next iterator of regular iterations

class Iterator:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop
    
    def __iter__(self):
        self.cur=self.start
        return self
    
    def __next__(self):
        if self.cur>= self.stop:
            raise StopIteration
        
        self.cur+=1
        return self.cur-1
    
custom_obj=Iterator(1,10)
ob_iter=iter(custom_obj)
print(next(ob_iter))
print(next(ob_iter))    
print(next(ob_iter))

lst=["A","B","C"]
lst_iter=iter(lst)
print(next(lst_iter))
print(next(lst_iter))
print(next(lst_iter))