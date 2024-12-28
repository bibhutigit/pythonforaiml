import numpy as np
import pandas as pd

my_numpy_arr = np.random.randn(5,4)
my_df = pd.DataFrame(my_numpy_arr,index=["A","B","C","D","E"],columns=["W","X","Y","Z"])
print("====Main DataFrame====")
print(my_df)

# Conditional selection
col_sel_df = my_df[my_df["W"] > 0]
print(col_sel_df)

# Multiple conditions
mul_cond_df = my_df[(my_df["W"] > 0) & (my_df["Y"] > 0)]
print(mul_cond_df)

# Adding a new column
my_state_list = ["CA", "NY", "WY", "OR", "CO"]
my_df["states"] = my_state_list
print(my_df)

# We set the states as index
my_df.set_index("states",inplace=True)
print(my_df)