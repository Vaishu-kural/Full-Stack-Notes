# ======================================
# 1. Animal → Dog (Single Inheritance)
# ======================================
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

dog = Dog()
dog.eat()
dog.bark()

# ======================================
# 2. Person → Employee, Student (Inheritance with Extra Attributes)
# ======================================
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

emp = Employee("Alice", 30, 50000)
stu = Student("Bob", 20, "A")
print(f"Employee: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
print(f"Student: {stu.name}, Age: {stu.age}, Grade: {stu.grade}")

# ======================================
# 3. Multilevel Inheritance (Device → Computer → Laptop)
# ======================================
class Device:
    def show_device(self):
        print("This is a device")

class Computer(Device):
    def show_computer(self):
        print("This is a computer")

class Laptop(Computer):
    def show_laptop(self):
        print("This is a laptop")

lap = Laptop()
lap.show_device()
lap.show_computer()
lap.show_laptop()

# ======================================
# 4. Hierarchical Inheritance (Shape → Triangle, Square)
# ======================================
class Shape:
    def display(self):
        print("This is a shape")

class Triangle(Shape):
    def area(self, base, height):
        return 0.5 * base * height

class Square(Shape):
    def area(self, side):
        return side * side

t = Triangle()
s = Square()
t.display()
print("Triangle Area:", t.area(10, 5))
print("Square Area:", s.area(4))

# ======================================
# 5. Method Overriding (Employee → Manager)
# ======================================
class Employee:
    def work(self):
        print("Employee is working")

class Manager(Employee):
    def work(self):
        print("Manager is managing the team")

m = Manager()
m.work()

# ======================================
# 6. Private Attribute Example (__pin)
# ======================================
class Account:
    def __init__(self):
        self.__pin = None

    def set_pin(self, pin):
        self.__pin = pin
        print("PIN set successfully")

    def validate_pin(self, pin):
        if self.__pin == pin:
            print("PIN is correct")
        else:
            print("Invalid PIN")

acc = Account()
acc.set_pin(1234)
acc.validate_pin(1234)

# ======================================
# 7. Encapsulation with Setter/Getter
# ======================================
class Car:
    def __init__(self):
        self.__speed = 0

    def set_speed(self, speed):
        if speed > 0:
            self.__speed = speed
        else:
            print("Invalid speed")

    def get_speed(self):
        return self.__speed

car = Car()
car.set_speed(120)
print("Car Speed:", car.get_speed())

# ======================================
# 8. Product with Discount
# ======================================
class Product:
    def __init__(self, price):
        self.__price = price

    def apply_discount(self, percent):
        if 0 < percent < 100:
            self.__price -= (self.__price * percent / 100)
        print("Discount Applied! Final Price:", self.__price)

p = Product(1000)
p.apply_discount(10)

# ======================================
# 9. Polymorphism (Bird and Duck both have fly)
# ======================================
class Bird:
    def fly(self):
        print("Bird is flying high")

class Duck:
    def fly(self):
        print("Duck is flying low")

def flying_test(obj):
    obj.fly()

b = Bird()
d = Duck()
for i in [b, d]:
    flying_test(i)

# ======================================
# 10. Loop Calling profession() (Doctor & Engineer)
# ======================================
class Doctor:
    def profession(self):
        print("I am a Doctor")

class Engineer:
    def profession(self):
        print("I am an Engineer")

for person in [Doctor(), Engineer()]:
    person.profession()

# ======================================
# 11. Operator Overloading (Time Addition)
# ======================================
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __add__(self, other):
        total_minutes = self.minutes + other.minutes
        extra_hour = total_minutes // 60
        minutes = total_minutes % 60
        hours = self.hours + other.hours + extra_hour
        return Time(hours, minutes)

    def show(self):
        print(f"{self.hours} hours and {self.minutes} minutes")

t1 = Time(2, 50)
t2 = Time(1, 30)
t3 = t1 + t2
t3.show()

# ======================================
# 12. Method Overloading using Default Parameters
# ======================================
class Greet:
    def say_hello(self, name1=None, name2=None):
        if name1 and name2:
            print(f"Hello {name1} and {name2}!")
        elif name1:
            print(f"Hello {name1}!")
        else:
            print("Hello!")

g = Greet()
g.say_hello()
g.say_hello("Alice")
g.say_hello("Alice", "Bob")

# ======================================
# 13. Abstract Class (Appliance → Fan, Light)
# ======================================
from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class Fan(Appliance):
    def turn_on(self):
        print("Fan is now ON")

class Light(Appliance):
    def turn_on(self):
        print("Light is now ON")

for a in [Fan(), Light()]:
    a.turn_on()

# ======================================
# 14. Abstract Class (Bank → SBI, HDFC)
# ======================================
class Bank(ABC):
    @abstractmethod
    def interest_rate(self):
        pass

class SBI(Bank):
    def interest_rate(self):
        return 7.5

class HDFC(Bank):
    def interest_rate(self):
        return 8.0

for bank in [SBI(), HDFC()]:
    print(f"{bank.__class__.__name__} Interest Rate: {bank.interest_rate()}%")

# ======================================
# 15. Abstract Class (Payment → CreditCard, UPI)
# ======================================
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

for p in [CreditCard(), UPI()]:
    p.pay(500)