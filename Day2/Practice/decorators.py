from functools import wraps
"""
    Create a decorator that prints "Starting..." before a function executes.
    Modify it to also print "Finished..." after execution.
    Create a decorator that prints the function's name before calling it.
"""

def toppings(func):

    @wraps(func)
    def wrapper():
        print(f"Your Order: {func.__name__}")
        print("Adding your toppings")
        func()
        print("Thank you visit again!!")
    
    return wrapper


@toppings
def cake():
    print("here is your cake !!")


# cake()

"=========================================================="

"""
    Write a decorator that counts how many times a function has been called.
"""

def counter(greet):
    count=0
    def wrapper():
        nonlocal count
        count+=1
        print(f"called {count} times")
    return wrapper

@counter
def greet():
    print("Hello")

# greet()
# greet()
# greet()
# greet()

"======================================================================"

"""
    Create a decorator that works with arguments.
"""

def deco(func):

    def wrapper(a,b):
        if(a<b):
            a,b=b,a
        return func(a,b)
    return wrapper


@deco
def div(a,b):
    return a//b


print(div(1,2))
