#abstract method & abstract class
#abstract class --> module
#ABC = Abstract Base Class
# from abc import ABC, abstractmethod

# class Car(ABC):
#     @abstractmethod         #@ is decorators
#     def moveForward(self):
#         pass

#     @abstractmethod
#     def moveBackward(self):
#       pass

#     # def moveBackward(self):
#     #     print("Hello")

#     @abstractmethod
#     def fm(self):
#         pass

# class Swift(Car):       #inherit
#     def moveForward(self):
#         print("Swift is moving forward")

#     def moveBackward(self):
#         #speed=30
#         #acceleration = speed*10
#         print("Swift is moving backward")

#     def fm(self):
#         print("Swift is playing fm")

# class Innova(Car):
#     def moveForward(self):
#         print("Innova is moving forward")

#     def moveBackward(self):
#         print("Innova is moving backward")

#     def fm(self):
#         print("Innova is playing fm")

# swift = Swift()
# swift.moveBackward()




from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class
    @abstractmethod
    def sound(self):  # Abstract method
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Using abstraction:
#d = Dog()
#print(d.sound())  # Output: Bark
c=Cat()
print(c.sound())

