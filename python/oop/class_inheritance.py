""" ALL ABOUT CLASS INHERITANCE """


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"I am a {self.name} and I am {self.age} years old")


# these classes are going to inherit the Animal Class Properties and Methods
class Cat(Animal):
    def speak(self):
        print("I say Meow")


class Dog(Animal):
    def speak(self):
        print("I say Bark")


# Cat instances
cat1 = Cat('Milo', 3)
cat1.show_details()
cat1.speak()

# Dog Instances
Dog1 = Dog('Rocky', 7)
Dog1.show_details()
Dog1.speak()


# Redefining attributes is a bad practice but can be refactored using the super().__init__() method

class Pet(Animal):
    def __init__(self, name, age, color):
        # This line tells the init to reference the attrs from the parent class i.e class Animal
        super().__init__(name, age)
        self.color = color


class Fish(Pet):
    def speak(self):
        print('Bubbles')


fish = Fish('Bubbles', 12, "Gold")

fish.show_details()
