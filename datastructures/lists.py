'''
    - Lists in python are mutable.
    - Lists can contain elements of different data types.
'''

# Declaring a list with different types
different_elem_lists = ["Hello", "Hi", 5, 6, 7, 25.9, True]
print(different_elem_lists)

# Accessing items of the lists
# Through indexes
first_item = different_elem_lists[0]
print(first_item)
# We can use negative index as well which retrieves elements from the last
last_item = different_elem_lists[-1]
print(last_item)

# Iterating over List
my_list = [1, 2, 3, 4, 5]
print(type(my_list))
for i in my_list:
    print(i)