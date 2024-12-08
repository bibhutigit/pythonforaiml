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

all_elems_excluding_first = different_elem_lists[1:]
print("All items excluding first", all_elems_excluding_first)

two_elems_starting_from_second_elem = different_elem_lists[1:3]
print("Two elements starting from second", two_elems_starting_from_second_elem)

# We can use negative index as well which retrieves elements from the last
last_item = different_elem_lists[-1]
print(last_item)


# Mutating the list
my_new_list = ["Hello", "Hi", "Bye"]
my_new_list[1] = "Hii"

print("After mutation", my_new_list)

# List methods
fruits = ["Apple", "Banana", "Orange", "Chiku"]
fruits.append("Grapes")
print("Fruits", fruits)

# Add to specific index
fruits.insert(1, "Pomegranate")
print(fruits)

fruits.append("Banana")
print(fruits.count("Banana"))

fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
fruits.reverse()
print(fruits)
fruits.clear()
print(fruits)

# Slicing List
double_colon_elems = different_elem_lists[::2] # Start from left with step size 2
print("Double colon",double_colon_elems)

double_colon_elems = different_elem_lists[::-1] # start from right with step size 1
print("Double colon",double_colon_elems)

# Iterating over List
my_list = [1, 2, 3, 4, 5]
print(type(my_list))
for number in my_list:
    print(number)

# Iterating with index
my_list = [1, 2, 3, 4, 5]
print(type(my_list))
for index,number in enumerate(my_list):
    print(index,number)

# List comprehension

# Basic List Comprehension
print([x*2 for x in range(10)])

# Conditional List comprehension
print([x*2 for x in range(10) if x%2==0])

# Nested List Comprehension
print([x*y for x in range(5) for y in range(4)])