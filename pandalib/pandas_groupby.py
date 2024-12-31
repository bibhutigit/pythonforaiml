import pandas as pd
import numpy as np

my_data = {"Company":["TCS","IBM","TCS","WIPRO","IBM","WIPRO"]
           ,"Person":["Bibhuti","Sourav","Plaban","Rajat","Manish","Lucky"]
           ,"Sales":[100,200,300,400,500,600]}

my_df = pd.DataFrame(my_data)
my_group_by_df = my_df.groupby("Company").count()
renamed_df = my_group_by_df.rename(columns={"Person":"person_count","Sales":"sales_count"})
my_reset_index_df = renamed_df.reset_index(names=["company"])
print(my_reset_index_df)

# Concatenate DFs
df1=pd.DataFrame({"A":["A0","A1","A2","A3"]
     ,"B":["B0","B1","B2","B3"]
     ,"C":["C0","C1","C2","C3"]
     },index=[0,1,2,3])

df2=pd.DataFrame({"A":["A4","A5","A6","A7"]
     ,"B":["B4","B5","B6","B7"]
     ,"C":["C4","C5","C6","C7"]
     },index=[4,5,6,7])

df3=pd.DataFrame({"A":["A8","A9","A10","A11"]
     ,"B":["B8","B9","B10","B11"]
     ,"C":["C8","C9","C10","C11"]
     },index=[8,9,10,11])

concatenated_df = pd.concat([df1,df2,df3])
print(concatenated_df)

# Merge DFS
# This actually done on a specific column
left = pd.DataFrame({"key":["K0","K1","K2"],"A":["A0","A1","A2"]})
right = pd.DataFrame({"key":["K0","K1","K3"],"B":["B0","B1","B2"]})

final_df = left.merge(right,how="right",on="key")
print(final_df)

# Join DFs
# It's done on the indexes
left_df = pd.DataFrame({"left_key":["K0","K1","K2"],"A":["A0","A1","A2"]},index=[0,1,2])
right_df = pd.DataFrame({"right_key":["K0","K1","K3"],"B":["B0","B1","B2"]},index=[0,1,3])

result_df = left_df.join(right_df,how="right")