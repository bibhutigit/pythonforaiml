def my_func(name):
    print(f"Hello {name}!! How are you!!")

def my_higher_order_func(name,my_func_arg):
    my_func_arg(name)

my_higher_order_func(name="Bibhuti",my_func_arg=my_func)