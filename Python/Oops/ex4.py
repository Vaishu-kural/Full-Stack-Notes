class Calculator:
    def __init__(self,a,b):
        self.n1=a
        self.n2=b
    def add(self):
        print("Add:",self.n1+self.n2)
    def sub(self):
        print("Sub",self.n1-self.n2)
    def mul(self):
        print("Mul",self.n1*self.n2)
    def div(self):
        print("Div",self.n1/self.n2)
obj1=Calculator(7,7)

obj1.add()
obj1.sub()
obj1.mul()
obj1.div()
