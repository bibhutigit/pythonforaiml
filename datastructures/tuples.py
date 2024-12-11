# Tuples are immutable
empty_tuple = tuple()
print(type(empty_tuple))

tuple_elems = tuple([1, 5, 6, 78])
print(tuple_elems)

# Accessing tuple elements
print(tuple_elems[0])

# Check immutability
my_tuple = (5, 8, 10)

# Common utility methods
print(my_tuple.count(5)) # count the number of occurrence of 5
print(my_tuple.index(8)) # Returns the first index of 8

# Packing and unpacking tuples
my_packed_tuple = ("Bibhuti",35,"bibhuti@gmail.com")

# Unpacking tuples
(name, age, email)= my_packed_tuple
print(name, age, email)

# unpacking with *
new_tuple = (1, 2, 3, 4, 5,6)
(first_elem,*rest_elems) = new_tuple
print(first_elem)
print(rest_elems)
(start,*middle,last) = new_tuple

