#doc: https://docs.python.org/3/howto/descriptor.html
class Ten:
    def __get__(self, obj, objtype=None):
        return 10

    # Here I created a __str__ function to prove that the get
    # descriptor has highter priority on object access
    def __str__(self):
        return "This is class Ten"

# To use the descriptor, it must be stored as a class variable in another class:
class A:
    x = 5                       # Regular class attribute
    y = Ten()  

a = A()
print(a.x)
print(a.y)
