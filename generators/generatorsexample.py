# A generator function is a special type of function which returns and iterator but lazily.
# So this is memory efficient and avoids entire list to be stored in memory rather return
# results when it is needed

# It is achieved through yield keyword which produce series of results over time
# when they are called/accessed.
# So the generator function generate values pause its execution after yield by maintaining
# its state between the iterations.

def my_num_cube_generator(n):
     for num in range(n):
         yield num**3

# So here if we loop through million items also then it will not be any memory issue.
for n in my_num_cube_generator(5):
    print(n)

def gen_fibo(n):
    a = 1
    b = 1

    for num in range(n):
        yield a
        a, b = b, a+b

print("Fibonacci Series")
for num in gen_fibo(10):
    print(num)

#iter() and next() demonstration

def int_val(num):
    for i in range(num):
        yield i

my_int_itr = int_val(10)

print(next(my_int_itr)) # Prints 0
print(next(my_int_itr)) # Prints 1
print(next(my_int_itr)) # # Prints 2
