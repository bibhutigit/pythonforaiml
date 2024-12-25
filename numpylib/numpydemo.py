import numpy as np
# NumPy Arrays
my_list = [[20,21,22,23,24],
           [25,26,27,28,29],
           [30,31,32,33,34]]
my_arr = np.array(my_list)
print(my_arr[0])

# Common way to create numpy array
my_range_arr = np.arange(1,11,2) #generate range arrays with step size 2
print(my_range_arr)

# If we want to generate 1-d or 2-d arrays with single digit
my_num_arr = np.ones((2,3)) #Creates a 2-d array with 2 rows and 3 columns
print(my_num_arr)

# Creating identity matrix with 1's in the diagonal and 0's elsewhere.
my_iden_matrix = np.eye(4)
print(my_iden_matrix)

# Generating random samples from a uniform distribution over 0 to 1 with specified dimension.
rand_numbers = np.random.rand(5)
print(rand_numbers)

print("Random integers in uniform distribution")
# Generating random samples from a low to high.
rand_int_numbers = np.random.randint(1,10, 10)
print(rand_int_numbers)

# Array re-shape. Distribute the array elements into specified dimension.
print("Re-shaping array")
my_int_arr = np.arange(10)
print(my_int_arr)
re_shaped_arr = my_int_arr.reshape(5,2)
print(re_shaped_arr)

# max and min element in an array.
max_elem = rand_int_numbers.max()
min_elem = rand_int_numbers.min()
print("Max and min elements in an array")
print(max_elem, "#", min_elem)

# Get indexes of the max and min elements.
print(rand_int_numbers)
max_index = rand_int_numbers.argmax()
min_index = rand_int_numbers.argmin()
print(max_index, "#", min_index)

#Datatype of array
print(rand_int_numbers.dtype)

# shape of an array
print("Shape of an array")
print(rand_int_numbers.shape)
reshaped_arr = rand_int_numbers.reshape(2,5)
print(reshaped_arr.shape)