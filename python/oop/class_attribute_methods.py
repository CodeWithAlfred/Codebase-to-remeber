""" ALL ABOUT STATIC CLASS METHODS AND ATTRIBUTES"""
# Class Properties
# These act like class constants, they do not change and are not instance specific


class Person:
    number_of_people = 0  # This is a static: Only to the class

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod  # Class methods
    def add_person(cls):
        cls.number_of_people += 1

    @classmethod
    def get_number_of_people(cls):
        return cls.number_of_people


p1 = Person('Alfred')
p2 = Person('Kevin')
p3 = Person('Victor')
print(p2.get_number_of_people())
