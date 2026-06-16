# Static methods = methods that are not related to one instance in specific,
# and as so can be accessed directly from the class

class Employee():
    def __init__(self, name, position):
        self.name = name
        self.position = position.lower()

    def get_info(self):
        return f"{self.name} - {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ['manager', 'cashier', 'cook', 'janitor']
        return position.lower() in valid_positions
    

employee1 = Employee("Eugene", "manager")
employee2 = Employee("Squidward", "cashier")
employee3 = Employee("Spongebob", "cook")

print(Employee.is_valid_position("rocket scientist"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())