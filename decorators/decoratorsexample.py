# Return function from another function

def hello(name="Jose"):
    print("Hello func starts!!")

    def greet():
        print("\t This is greet method!!")

    def welcome():
        print("\t This is welcome method!!")

    if name == "Jose":
        return greet
    else:
        return welcome

my_greet_func = hello()
my_welcome_func = hello("Jack")

my_greet_func()
my_welcome_func()

# Passing function as an argument

def greetPerson(name):
    print(f"Hello {name}!!")

def hello(name,greetFunc):
    greetFunc(name)

hello("Bibhuti",greetPerson)

# Decorator function illustration
def my_decorator_func(original_func):
    def wrapper_func():
        print("Some functionality before the original function!!")
        original_func()
        print("Some work after the original function!!")

    return wrapper_func

def func_need_decorator():
    print("I want to be decorated!!")

decorated_func = my_decorator_func(func_need_decorator)
decorated_func()

# The above calling can be done using below annotation

@my_decorator_func  # This means pass below function into my_decorator_func as argument
def my_func_needs_decorator():
    print("I want to be decorated!!")

my_func_needs_decorator()
