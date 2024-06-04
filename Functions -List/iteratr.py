# Iterator
# iter()
from bakarSecure import check_email_secure, check_password


# pip install .\bakarSecure-0.1-py3-none-any.whl
# python setup.py sdist bdist_wheel
# cd .\dist
# pip install twine
# twine check dist\*
# twine upload dist/*   


class my_iter:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop
        
    def ___iter__(self):
        self.cur=self.start
        return self
    
    def __next__(self):
        if self.cur>=self.stop:
            raise StopIteration 
        self.cur+=1
        return self.cur-1

def example():  
    custom_ob=my_iter(1,10)
    obj=iter(custom_ob)
    print(obj)
    for num in obj:
        print(num)
        
    
example()
    


    