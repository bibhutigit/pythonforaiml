# Creating an empty dictionary

empty_dict = {}
print(empty_dict)

another_empty_dict = dict()
print(another_empty_dict)

print(type(empty_dict), type(another_empty_dict))

dict_with_elems = dict({"Name": "Bibhuti", "Age": 37, "Address": "Jajpur"})
print(dict_with_elems)

# Accessing elements from dictionary
print(dict_with_elems["Name"])
print(dict_with_elems.get("Name"))
print(dict_with_elems.get("LName"))  # Set a default
print(dict_with_elems.get("LName", "Not Available"))  # Set a default value

# Dictionaries are mutable
dict_with_elems["Name"] = "Jacob"
print(dict_with_elems.values)

# Accessing the dictionary keys and loop through it
for key in dict_with_elems.keys():
    print(dict_with_elems.get(key))

# Delete key from dictionary
del dict_with_elems["Name"]
print(dict_with_elems)

# Items which returns as key value tuples
for key, value in dict_with_elems.items():
    print(key, value)

# Shallow and Deep copy dictionary
student_dict = {"name": "Bibhuti", "Age": 37, "Email": "bibhuti@gmail.com"}
shallow_student_dict = student_dict
student_dict["name"] = "Jack"  # It will change the another_student_dict as well
print(student_dict)
print(shallow_student_dict)
deep_student_dict = student_dict.copy()
student_dict["name"] = "Bibhuti"
print(student_dict)
print(deep_student_dict)

# Nested dictionaries
nested_dictionary = {
    "name": "Bibhuti",
    "age": 35,
    "address": {
        "plot_no": "3155/234",
        "city": "Jajpur Road",
        "dist": "Jajpur",
        "state": "Odisha"
    }
}
print(nested_dictionary)

# Access nested dictionaries
plot_no = nested_dictionary["address"]["plot_no"]
print(plot_no)

# Print all the address details
for add_key, add_value in nested_dictionary["address"].items():
    print(add_key, add_value)

# Dictionary Comprehensions
my_updated_dict = {key: ("Soumya" if value == "Bibhuti" else value) for key, value in student_dict.items()}
print(my_updated_dict)

# Use dictionary to count the frequency of the elements in the list.
my_num_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
count_dict={}
#result_dict = { num:(count_dict.get(num)+1 if num in count_dict else count_dict[num]1) for num in my_num_list}

for num in my_num_list:
    if num in count_dict:
        count_dict[num] = count_dict[num]+1
    else:
        count_dict[num] = 1

print(count_dict)