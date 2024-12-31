import pandas as pd

def mul_each_elem_by_two(elem):
    return elem * 2

data_dict = {"col_1":[1,2,3,4]
             ,"col_2":[444,555,666,444]
             ,"col_3":['abc','defg','hi','jklmn']}

my_df = pd.DataFrame(data_dict)

# Get array of unique elements from a dataframe columns
unique_elems = my_df["col_2"].unique()

# Get number of unique elements
unique_elems_count = my_df["col_2"].nunique()
print(unique_elems_count)

# Individual counts of unique elements
value_counts = my_df["col_2"].value_counts()
print(value_counts)

# apply method demonstration
# apply custom methods to one column
my_applied_df = my_df["col_1"].apply(mul_each_elem_by_two)
print(my_applied_df)

#applying in-built method
my_len_df = my_df["col_3"].apply(len)
print(my_len_df)

#applying any lambda method
my_mul_df = my_df["col_1"].apply(lambda x : x*5)
print(my_mul_df)

#sort column values
sort_values = my_df.sort_values("col_3")
print(sort_values)

