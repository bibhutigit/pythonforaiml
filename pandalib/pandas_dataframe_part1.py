import pandas as pd
import numpy as np

rand_data = np.random.randn(3, 2)
print(rand_data)
my_indexes = ["A", "B", "C"]
my_cols = ["X", "Y"]

my_df = pd.DataFrame(rand_data, my_indexes, my_cols)
print(my_df)

# Creating as new column
my_df["derived_col"] = my_df["X"] + my_df["Y"]
print(my_df)

#Dropping that column
my_df.drop("derived_col",axis=1) # This statement will not affect the original my_df
print(my_df)

# To make the column drop effective to original my_df we need to use inplace flag.
my_df.drop("derived_col",axis=1,inplace=True)
print(my_df)

# We can same way drop rows
my_df.drop("C",axis=0,inplace=True)
print(my_df)

# Selecting Columns
selected_df = my_df["X"]
print(selected_df)
print("======")
# Selecting Rows
# By locating the actual labels of the row
labelled_row = my_df.loc["B"]
print(type(labelled_row))
# By locating the actual index of the row
indexed_row = my_df.iloc[1]
print(type(indexed_row))

print("======")
# We can get subset of data by passing both rows and columns
selected_row_col_value = my_df.loc[["B"],["X"]]
print(selected_row_col_value)
print(type(selected_row_col_value))