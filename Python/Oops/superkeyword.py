#child class to parent class access 
class a():
    def __init__(self):
        print("A")

    def display(self):
        print("u r in class a")

class b(a):
    def __init__(self):
        print("B")
        super().__init__()

    def display(self):
        print("u r in class b")

ob1=b()
