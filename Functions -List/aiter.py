# Asynchronous Iterator
# aiter()

import asyncio

class AsyncIteration():
    # it take starting and stopping value of iteration.

    def __init__(self,start,stop):
        self.start=start
        self.stop=stop
    
    def __aiter__(self):
        self.cur=self.start
        return self
    
    async def __anext__(self):
        await  asyncio.sleep(1)
        if self.cur >=self.stop:
            raise StopAsyncIteration
        
        self.cur+=1
        return self.cur -1
    
    
async def example():
    custom_obj=AsyncIteration(1,11)
    obj_iter=aiter(custom_obj)
    print(obj_iter)
    async for num in obj_iter:
            print(num)
            
asyncio.run(example())
# Output 
# <__main__.AsyncIteration object at 0x0000020EF4E931D0>
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9 
# 10