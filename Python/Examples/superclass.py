class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person name is {self.name}")

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)  # Call parent class constructor
        self.grade = grade
        print(f"Grade is {self.grade}")

s1 = Student("Alice", "A")
