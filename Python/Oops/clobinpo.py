#1
'''class shape():
    def area(self):
        return 0

class rectangle(shape):
    def area(self):
        l=10
        b=20
        print(l*b)

r1=rectangle()
r1.area()

#s1=shape() -->1
#print(s1.area())
'''

#2
class Person():
    def __init__(self,name):
        self.name=name

class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name) 
        self.grade=grade

    def display(self):
        print(self.name,self.grade)

s1=Student("vaishu","A grade")
s1.display() 
