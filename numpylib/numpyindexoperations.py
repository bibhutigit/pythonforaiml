import numpy as np

my_numpy_arr = np.arange(1, 11)
print(my_numpy_arr)

# Accessing through indexes
my_elem = my_numpy_arr[5]
print(my_elem)

range_of_elems = my_numpy_arr[1:5]
print(range_of_elems)
range_of_elems = my_numpy_arr[1:]
print(range_of_elems)

# Assigning one single value to a range of elements
range_of_elems[1:5] = 200

# Deep and shallow copy of array
print(range_of_elems) # This is in fact shallow copy.
                      # So, though we change the portion of the array it actually
                      # changed the original one.
print(my_numpy_arr)
copied_numpy_arr = my_numpy_arr.copy()
copied_numpy_arr[:] = 500
print(my_numpy_arr)
print(copied_numpy_arr)

# Indexing and selection 2-d array
my_2d_arr = np.array([[5,10,15],[10,12,14],[25,35,80]])
print(my_2d_arr)

print(my_2d_arr[0,1]) # through comma
print(my_2d_arr[0][2])# through double brackets

# Getting sub matrix
# Getting bottom left corner matrix like below
# [10, 12
#  25,35]
sub_matrix_arr = my_2d_arr[1:,:2]
print(sub_matrix_arr)

# Conditional selection
print(my_numpy_arr)
filtered_arr = my_numpy_arr[my_numpy_arr >= 8]
print(filtered_arr)