class Animal:
    def __init__(self):
        print("Animal called!!")

    def who_am_i(self):
        print("I am an Animal!!")


class Dog(Animal):
    def __init__(self, breed, name):
        Animal.__init__(self)
        self.breed = breed
        self.name = name

    def who_am_i(self):
        print("I am a Dog!!!")

my_dog = Dog("Labrador", "Oscar")
my_dog.who_am_i()