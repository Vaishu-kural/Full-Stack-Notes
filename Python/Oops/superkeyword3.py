class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call the parent class constructor
        self.student_id = student_id
        print(f"Student ID: {self.student_id}")

# Create object of Student class
s = Student("Alice", 20, "S123")
