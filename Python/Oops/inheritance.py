#Single Inheritance
class dad():
    def phone(self):
        print("Dad's phone")

class son(dad):
    def laptop(self):
        print("Son's Laptop")

ram=son()
#ram.laptop()
ram.phone()

