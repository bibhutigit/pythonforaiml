import pandas as pd
from fontTools.merge.util import avg_int

# Pandas have two datastructures
    # Series (1-dimensional)
    # DataFrame (2-dimensional)
csv_data = pd.read_csv("./weather_data.csv")
csv_data["location"] = "Delhi" #Adding one extra column to it with default value
print(csv_data)

print(type(csv_data)) # It's DataFrame type

#Get data of a single column
temperatures = csv_data["temp"]

# Alternative way
panda_temp_series = csv_data.temp # Here pandas converts all the columns into attributes.
print("Temperatures Series", panda_temp_series)
print(temperatures)
print(type(temperatures)) # It's a Series type

# Convert from pandas into python data structures
temp_list = temperatures.to_list()
print(temp_list)

# Find out max temperatures
max_temp = temperatures.max()
print(max_temp)
# Find out average temperatures in hard way
avg_temp = sum(temp_list) / len(temp_list)

# Find out average temperatures through panda series API
avg_temp_mean = temperatures.mean()

# mean temperatures
print(avg_temp)
print(avg_temp_mean)

# Filter data in pandas
# If we set only column name in panda dataframe we will get all the values for that column
# But if we add one condition then we will get rows.
monday_data = csv_data[csv_data.day == "Monday"]
print(monday_data)

# Find the day with maximum temperature
max_temp_day = csv_data[csv_data.temp == csv_data.temp.max()]
print(max_temp_day)
print(type(max_temp_day)) # DataFrame type

print("Monday temp data")
# Get the temperature of Monday converted into Celsius
monday_temp_data = csv_data.temp[csv_data.day == "Monday"]
print(monday_temp_data)
print(type(monday_temp_data)) # Series type
print(monday_temp_data[0]/32)

# Convert all the values of temperatures from Fahrenheit into Celsius
csv_data["temp"] = csv_data.temp/32

sel_cols = csv_data[["day","temp","condition"]]
print(sel_cols)

