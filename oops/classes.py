class Sample:
    pass

sample1 = Sample()
sample2 = Sample()

print(type(sample1))
print(type(sample2))

class Employee:
    def __init__(self,name,age,email):
        # instance variables
        self.ename = name # we can use any name as attribute but, it's recommended to give same name as the parameter
        self.eage = age
        self.eemail = email

    def join(self):
        print(f"Hello {self.ename}, thanks for joining!!!")

emp_bibhuti = Employee("Bibhuti",37,"bibs.mohapatra@gmail.com")
print(emp_bibhuti.ename)
emp_bibhuti.join()


class Dog:
    #Class level attribute. It's same for every instance of a class
    animal_class = "mammal"
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


my_dog = Dog(breed="Lab", name="Oscar")
my_other_dog = Dog(breed="Pomeranian", name="Sheru")

print(my_dog.animal_class)
print(my_other_dog.animal_class)
print(Dog.animal_class) #We can access through class name as well. This is more conventional.


