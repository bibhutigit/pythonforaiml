import math
import numpy as np  # use alias
import array as arr
# For specific function
from math import sqrt, pi
from custompackage.mycustommath import add  # In this way we can create subpackages as well

print(math.sqrt(20))
print(sqrt(16))
print(pi)

my_np_array = np.array([1, 2, 3, 4, 5])
print(my_np_array)

print(add(5, 8))  # Calling custom package methods

my_arr = arr.array("i", [1, 2, 3])
print(my_arr)

for i in my_arr:
    print(i)