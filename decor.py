def my_decorator(some_function):

    def wrapper():
	print("before")
        some_function()
        print("after")

    return wrapper

@my_decorator
def just_some_function():
    print("function stuff")

just_some_function()

