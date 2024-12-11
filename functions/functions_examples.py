# Illustration of any()
# It returns True if any one of the item in the given iteration is True or False.
lst = [False, False, False, False]
print(any(lst))

other_lst = [False, False, True, False]
print(any(other_lst))

# Lambda functions
add_two_int = lambda a,b:a+b
print(add_two_int(5,5))

# map function
doubly_list = list(map(lambda x:x**2,range(5)))
print(doubly_list)

# typecasting using map functions
str_numbers = ['1','2','3','4','5','6']
int_numbers = list(map(int,str_numbers)) # here int is a method applied to all char to convert them
print(int_numbers)

# filter function
students = [
    {"name":"Bibhuti", "age":37}
    ,{"name":"Plaban", "age":37}
    ,{"name":"Soumya", "age":38}
    ,{"name":"Sambit", "age":21}
]

# filter students less than 25
filtered_students = list(filter(lambda student:student["age"]<25,students))
print(filtered_students)