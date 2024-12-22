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

