# Basics concepts on oop

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")


car_1 = Car("Mustang", 2026, "red", False)
car_2 = Car("Corvette", 2025, "blue", True)
car_3 = Car("Charger", 2027, "yellow", True)

car_1.describe()
car_2.describe()
car_3.describe()