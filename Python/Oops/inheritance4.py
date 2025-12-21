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
