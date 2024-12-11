# Set declaration
my_set = {1,2,2,3,4}
print(my_set)

# Create empty set
empty_set = set()
print(empty_set)

# Declare set using set constructor
set_elems = set([1,3,4,5,5,6,6])
print(set_elems)

# Check element existence in Set
print(4 in set_elems)

# Math operations
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))