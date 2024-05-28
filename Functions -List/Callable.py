# Callable
# callble()
# It checks if the given parameter is a function
# or can be to execute

class check:
    def __init__(self):
        pass

def why():
    print("why are you here?")

def outer():
    def inner():
        pass
    return inner
    
anonymous=lambda x:x+1
no_function='No'

print(callable(check))
print(callable(why))
print(callable(outer()))
print(callable(anonymous))
print(callable(no_function))
# True
# True
# True
# True
# False