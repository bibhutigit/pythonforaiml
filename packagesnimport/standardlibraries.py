import os
import shutil
import json
import csv
from datetime import datetime,timedelta
import re

# os related operation
print(os.getcwd())
#os.mkdir("test_dir")

# Operations on files
#shutil.copy("source.txt","destination.txt")

# Data serialization
#Sample json operations
data = {"name":"Bibhuti", "age":35, "email":"bibhuti@gmail.com"}
print(type(data))
jsonstr = json.dumps(data)
print(jsonstr,type(jsonstr))
dict_data = json.loads(jsonstr)
print(type(dict_data))

# csv utility
with open("sample.csv",mode="w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(['name','age'])
    writer.writerow(['Bibhuti',35])

with open("sample.csv",mode="r") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)

# datetime
now = datetime.now()
last_day = now-timedelta(days=1)
print(now, last_day)

#Regular Expression
pattern = r'\d+'
text = "123 string"
match = re.search(pattern,text)
print(match.group())