#doc: https://www.geeksforgeeks.org/args-kwargs-python/
def myFun(arg1, **kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))


# Driver code
myFun("Hi", first='Geeks', mid='for', last='Geeks')



def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
 
 
# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)
 
kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)
