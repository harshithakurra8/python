#Decorator function
def fence(func):
    def add_fenc(val):
        print("+"*10)
        func(val)
        print("+"*10)
    print("returning add_fence")
    return add_fenc
@fence
def log(val):
     print(val) 

#Creating decorating functions
def fence(func):
    def add_fenc(val):
        print(f"add_fenc({val})called!")
        print("+"*10)
        func(val)
        print("+"*10)
    return add_fenc
@fence
def log(val):
    print(f"log({val})called!")
    print(val)

#Factorial

def factorial(n):
    if n == 0 or n == 1:
        return n
    else:
        return n*factorial(n-1)

print(factorial(5))

#function tools.partial function
from functools import partial
square=partial(pow, exp=2)
cube=partial(pow, exp=3)

#wraps decorator
from functools import wraps
def decorator(func):
    @wraps(func)
    def processor():
        func()
    return processor
@decorator
def somefunc():
    """docstring of somefunc"""
    return 0
