# Class variables = variables that are equal for all instances of a class

class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

        Student.num_students += 1

    
student_1 = Student("Spongebob", 30)
student_2 = Student("Patrick", 35)
student_3 = Student("Squidward", 55)
student_4 = Student("Sandy", 27)

print(Student.num_students)