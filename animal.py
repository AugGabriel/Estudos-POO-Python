# Inheritance = a class can inherit methods and attributes from a parent

class Animal:
    def __init__(self, name, is_alive=True):
        self.name = name
        self.is_alive = is_alive

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")


class Dog(Animal):
    def speak(self):
        print("WOOF!")


class Cat(Animal):
    def speak(self):
        print("MEOW!")


class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")


dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

mouse.speak()