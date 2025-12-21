# Parent class
'''class Animal:
    def sound(self):
        print("Animals make different sounds")
#an1= Animal()
#an1.sound()
# Child class (inherits from Animal)
class Dog(Animal):
    def sound(self):
        #print("Woof! Woof!")
        pass
class Cat(Animal):
    def sound(self):
        print("Meow!")
class Parrot(Animal):
    def sound(self):
        print("kee kee")
# Objects
dog1 = Dog()
cat1 = Cat()
p1=Parrot()
dog1.sound()   # Output: Woof! Woof!
cat1.sound()   # Output: Meow!
p1.sound()
'''
#Single
#base class
'''class dad:
    def phone(self):
        print("Dad's phone")
#derived class
class son(dad):
    def laptop(self):
        print("Son's Laptop")
#ram=son()
#ram.laptop()
#ram.phone()
d1=dad()
d1.phone()
#d1.laptop()'''

#Multiple Inheritance
#base class1
'''class dad():
    def phone(self):
        print("Dad's phone")
#base class2
class mom():
    def sweet(self):
        print("Mom's Sweet")
class son(dad,mom):
    def laptop(self):
        print("Son's Laptop")
ram=son()
ram.laptop()
ram.phone()
ram.sweet()
'''
#Multilevel Inheritance
'''class grandpa():
    def phone(self):
        print("grandpa's phone")

class dad(grandpa):                    #class dad(grandpa):
    def money(self):
        print("dad's money")

class son(dad):                    #class son(dad):
    def laptop(self):
        print("son's laptop")

ram = son()
ram.laptop()
ram.money()
ram.phone()
'''
#d1=dad()
#d1.phone()
#ram.phone()     # ==> multilevel inheritance

#Hierarchical Inheritance
class dad():
    def money(self):
        print("dad's money")
class son1(dad):
    pass
class son2(dad):
    pass
class son3(dad):
    pass
s3=son3()
s3.money()

s2=son2()
s2.money()
