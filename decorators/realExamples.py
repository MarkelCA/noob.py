import functools
import time

# Technical Detail: The @functools.wraps decorator uses 
# the function functools.update_wrapper() to update special 
# attributes like __name__ and __doc__ that are used in the introspection.

###################
## TIMER
##################
def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      
        run_time = end_time - start_time    
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

@timer
def timed_sleep():
    time.sleep(2)

# waste_some_time(1000)
# timed_sleep()

###################
## DEBUG
##################
def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  
        signature = ", ".join(args_repr + kwargs_repr)           
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           
        return value
    return wrapper_debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"
x = make_greeting(name='Marke')
print(x)



###################
## LOGIN REQUIRED
##################
# from flask import Flask, g, request, redirect, url_for
# import functools
# app = Flask(__name__)

# def login_required(func):
    # """Make sure user is logged in before proceeding"""
    # @functools.wraps(func)
    # def wrapper_login_required(*args, **kwargs):
        # if g.user is None:
            # return redirect(url_for("login", next=request.url))
        # return func(*args, **kwargs)
    # return wrapper_login_required

# @app.route("/secret")
# @login_required
# def secret():
    # pass

###################
## SINGLETON
##################
def singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton

@singleton
class TheOne:
    pass

first = TheOne()
second = TheOne()
print(id(first))
print(id(second))
