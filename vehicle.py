# Abstract classes = classes and methods that cannot be instantiated
# Abstract methods = they have to be developed in the child class, in order for the
# class to be allowed to be instantiated

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")


class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")


class Boat(Vehicle):
    
    def go(self):
        print("You sail the boat")

    def stop(self):
        print("You anchor the boat")


boat = Boat()
boat.go()
boat.stop()