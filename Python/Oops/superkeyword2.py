class a():
    def __init__(self):
        print("A")

    def display(self):
        print("u r in class a")

class b():
    def __init__(self):
        super().__init__()
        print("B")

    def display(self):
        print("u r in class b")

class c(b,a):          #multiple inheritance(a,b)
    def __init__(self):
        super().__init__()
        print("C")

    def display(self):
        print("u r in class c")
ob1=c()

'''ob1 = c()

c.__init__() is called.

Inside c.__init__, super().__init__() calls b.__init__().

Inside b.__init__, super().__init__() calls a.__init__().

a.__init__() prints: A

b.__init__() prints: B

c.__init__() prints: C'''