def my_func():
    print("My first function")

my_func()

# Function with return statement

def add(a, b):
    return a+b

print(add(5,7))

# Default parameters
def greet(name="Guest"):
    print(f"Hello {name}")

greet("Bibhuti")

# Variable length arguments
def var_ag_func(name,*other_details):
    print(name)
    print(other_details)

var_ag_func("Bibhuti",35,"bibs.mohapatra@gmail.com")


# Keyword Argument
def print_details(**kwargs):
    for key,value in kwargs.items():
        print(key, value)

print_details(name="Bibhuti",age=40,email="bibs.mohapatra@gmail.com")

# Demonstrating both positional and keyword arguments
def print_all(*args, **kwargs):
    for num in args:
        print(num)

    for key,value in kwargs.items():
        print(key, value)

print_all(1,2,3,4,5,name="Bibhuti",age=40,email="bibs.mohapatra@gmail.com")