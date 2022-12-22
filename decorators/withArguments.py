#doc: https://realpython.com/primer-on-python-decorators/
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")

greet(name='Markel')

# With return:
def do_thrice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_thrice
def greet3(name):
    print(f"Hello {name}")
    return('How are you')
print(greet3('Sam'))
