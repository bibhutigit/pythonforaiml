import numpy as np

# Create an array of 10 zeros
arrays_with_zeros = np.zeros(10)
print(arrays_with_zeros)

# Create an array of 10 ones
arrays_with_ones = np.ones(10)
print(arrays_with_ones)

# Create an array with 5s
arrays_with_fives = np.arange(10)
arrays_with_fives[:] = 5
print(arrays_with_fives)

# Alternative way
alternate_way_of_fives = np.ones(10) * 5
print(alternate_way_of_fives)

# Create an array of integers from 10 to 50
num_arr = np.arange(10, 51)
print(num_arr)

# Create an array of all the even integers from 10 to 50
even_num_arr = num_arr[num_arr % 2 == 0]
print(even_num_arr)
# Alternate way to do this
alter_num_arr = np.arange(10, 51, 2)
print(alter_num_arr)

# Create a 3 x 3 matrix
int_arr = np.arange(0,9)
int_matrix = int_arr.reshape(3,3)
print(int_matrix)

# Create a 3x3 identity matrix
iden_matrix = np.eye(3)
print(iden_matrix)

# Random number from 0 to 1
rand_num = np.random.rand(1)
print(rand_num)

# Generate an array of 25 random numbers sampled from standard normal distribution.
random_nums = np.random.randn(25)
print(random_nums)

#Or
range_nums_arr = np.arange(0.01, 1.01, 0.01)
reshaped_arr = range_nums_arr.reshape(10,10)

#Or
other_range_nums_arr = np.arange(1, 101).reshape(10,10)/100
print(other_range_nums_arr)

#Or via linspace()
print("linspace array")
linspace_arr = np.linspace(0.01,1,100).reshape(10,10)
print(linspace_arr)
