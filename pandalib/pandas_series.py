# panda Series are one-dimensional labeled array with any type of data.
# It's built on top of NumPy.

import pandas as pd
import numpy as np

labels = ["Bibhuti", "Plaban", "Soumya"]
data = [30, 40, 50]
numpy_arr = np.array(data)
my_data_dict = {"Bibhuti": 30, "Plaban": 40, "Soumya": 50}

# Creating Series with integer list
# Here the indexes will be by default integer like the way in arrays
my_data_series = pd.Series(data)

# Changing the indexes by applying labels.
my_data_series = pd.Series(data,labels)

# Applying it to numpy array.
my_data_series = pd.Series(numpy_arr,labels)

# Creating Series from dictionaries
my_data_series = pd.Series(my_data_dict)
print(my_data_series)

# Accessing elements from Series.

print(my_data_series["Bibhuti"])