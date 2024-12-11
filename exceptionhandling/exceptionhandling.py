# a = 10
# b = 0
# c = a/b
# print(c)
try:
    a = 5
    b = 2
    c = a/b
    d = 5
    a = d
except ZeroDivisionError as zd:
    print("Number can't be divided by zero.", zd)
except NameError as ne:
    print("Number is not defined.", ne)
except Exception as e:
    print(e)
else:
    print("This will be executed if no error is thrown")
finally:
    print("This will be executed at last anyways")