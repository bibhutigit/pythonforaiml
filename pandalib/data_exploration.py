import pandas as pd

salaries_df = pd.read_csv("./salaries_by_college_major.csv")
print(salaries_df)

columns = salaries_df.columns

for column in columns:
    print(column)

# Check na columns
data_df = salaries_df.isna()[["Undergraduate Major","Starting Median Salary","Mid-Career Median Salary"]]

# Drop na columns
drop_na_df = salaries_df.dropna()
print(drop_na_df)

# Get all the columns where starting median salary is maximum
median_salary_df = drop_na_df[drop_na_df["Starting Median Salary"] == drop_na_df["Starting Median Salary"].max()]
print(median_salary_df)

# Another way to get max starting median salary
id_max = drop_na_df["Starting Median Salary"].idxmax() # Get index of the maximum "Starting Median Salary"
max_under_graduate_major_df = drop_na_df["Undergraduate Major"].loc[id_max] # Get the Major of the maximum median salary
print(max_under_graduate_major_df)