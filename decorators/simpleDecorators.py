print('----------------Simple decorator----------------')
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

decorated_say_whee = my_decorator(say_whee)
decorated_say_whee()
print()
print('----------------With sintactic sugar----------------')

def my_decorator2(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator2
def decorated_say_whee2():
    print("Whee!")

decorated_say_whee2()

