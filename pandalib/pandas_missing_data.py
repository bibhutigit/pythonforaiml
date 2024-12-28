import numpy as np
import pandas as pd

my_dict = {"A":[1,2,3],"B":[1,2,np.nan],"C":[1,np.nan,np.nan]}
my_df = pd.DataFrame(my_dict)
print(my_df)

my_df.dropna()
print(my_df) # it will drop the rows where we get at least one NaN value.

# We can check threshold as well.
my_df.dropna(thresh=2,inplace=True)
print(my_df)

my_df.fillna(value=0,inplace=True)
print(my_df)