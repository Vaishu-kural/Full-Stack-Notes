class a():
    def __init__(self):
        print("A")
    def display(self):
        print("this is a class")

class b(a):
    def __init__(self):
        super().__init__()
        print("B")
    def display(self):
        print("this is a b class")

obj = b()
