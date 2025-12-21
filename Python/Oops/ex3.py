class teacher:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def display(self):
        print("Name:",self.name)
        print("Register Number:",self.regno)

t1 = teacher("Vaishu","003")
t2 = teacher("Janu","004")

t1.display()
t2.display()

