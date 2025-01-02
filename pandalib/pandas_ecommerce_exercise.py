import pandas as pd

ecom = pd.read_csv("Ecommerce_Purchases.csv")

# Dataframe columns
print(ecom.columns)

# Get the head of the dataframe
head_df = ecom.head()
print(head_df)

# Get how many rows and columns in a dataframe
print(len(ecom.columns)) # Get number of columns
print(ecom.columns.size) # Get number of columns
print(ecom.shape[1]) # Get number of columns

print(len(ecom.index)) # Get number of rows
print(ecom.shape[0]) # Get number of rows

# Average purchase price
avg_purchase_price = ecom["Purchase Price"].mean()
print(avg_purchase_price)

# Highest and Lowest purchase price
low_purchase_price = ecom["Purchase Price"].min()
high_purchase_price = ecom["Purchase Price"].max()
print(low_purchase_price)
print(high_purchase_price)

# English 'en' as choice of language
language_count = ecom[ecom["Language"] == "en"]["Address"].count()
print(language_count)

# How many people have job title "Lawyer"
job_title_count = ecom[ecom["Job"] == "Lawyer"]["Job"].count()
print(job_title_count)

# How many people made purchase during AM and PM
AM_PM_count = ecom.value_counts("AM or PM")
print(AM_PM_count["AM"]) # AM count
print(AM_PM_count["PM"]) # PM count

# 5 most common job title
job_title_count = ecom.value_counts("Job").sort_values(ascending=False)
print(job_title_count.head(5))

# How many people have a credit card that expires in 2025
expiry_date_df = ecom[ecom["CC Exp Date"].apply(lambda x: x[3:] == '25')].count()
print(expiry_date_df)

