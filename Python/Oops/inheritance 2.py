#Multiple Inheritance
class dad():
    def phone(self):
        print("Dad's phone")

class mom():
    def sweet(self):
        print("Mom's Sweet")

class son(dad,mom):
    def laptop(self):
        print("Son's Laptop")

ram=son()
#ram.laptop()
ram.phone()
ram.sweet()
