class Animal:
    animalType = "Mammal"

class Pet:
    color = "White"

class Dog:
    @staticmethod
    def bark():
        print("Bow Bow!")

d = Dog()
d.bark()