#Encapsulation

'''class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
# Object
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# print(account.__balance)  # ❌ Error: Cannot access private variable directly
'''

'''class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


# Runtime input
initial_balance = float(input("Enter initial balance: "))
account = BankAccount(initial_balance)

deposit_amount = float(input("Enter deposit amount: "))
account.deposit(deposit_amount)

print("Final Balance:", account.get_balance())'''

#Polymorphism

'''class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

# Using polymorphism
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound()) '''


from abc import ABC, abstractmethod

# Abstract class
'''class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass   # Only idea, no implementation

# Car must implement start()
class Car(Vehicle):
    def start(self):
        print("Car engine starts with a key")

# Bike must implement start()
class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self start button")

# Using abstraction
v1 = Car()
v2 = Bike()
v1.start()
v2.start()

'''
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # method without implementation

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

# Objects
sq = Square(5)
cr = Circle(3)

print("Square Area:", sq.area())   # Output: 25
print("Circle Area:", cr.area())   # Output: 28.26
