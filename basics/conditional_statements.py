age = 30
if age >= 18:
    print("You are an adult")
elif age <= 18:
    print("You are a minor")

# Nested conditional statements

num = -1

if num >= 0:
    print("It's a positive number and let's check further whether it's even or odd!!")
    if num % 2 == 0:
        print("It's an even number!!")
    else:
        print("It's an odd number!!")

else:
    print("It's a negative number!!")

# Check if a year is a leap year or not.
year = 1996

if year >= 0:
    if year % 4 == 0:
        print("This year is a leap year!!")