class Animal():
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):    #method override
        print("Dog Barks")

class Birds(Animal):
    def sound(self):
        print("Birds Sing")

#a1=Animal()
#a1.sound()

#d1=Dog()
#d1.sound()

b1=Birds()
b1.sound()
'''Concept	Description
Inheritance	Dog and Birds inherit from the Animal class.
Method Overriding	Both child classes redefine the sound() method of the parent class.
Polymorphism	Even though sound() is defined in multiple classes, the correct version is called depending on the object (Dog, Birds, etc.).'''