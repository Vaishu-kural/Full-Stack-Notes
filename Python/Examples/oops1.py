'''class Car():
    # Attribute/variables
    brand = "Toyota"
    color = "Red"
# Creating object
my_car = Car()
# Accessing attributes
print("Brand:", my_car.brand)
print("Color:", my_car.color)
'''
'''class phone():
    def __init__(self,brand,price,ram):
        self.brand=brand
        self.price=price
        self.ram=ram
    def display(self):
        print("Brand: ",self.brand)
        print("Price: ",self.price)
        print("RAM: ",self.ram)
oppo=phone("Oppo","15000","16gb")
vivo=phone("Vivo",20000,"8gb")
oneplus=phone("one+",20000,"16gb")
oppo.display()
vivo.display()
oneplus.display()'''

'''
class phone():
    chargetype="C-TYPE"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("\nBrand: ",self.brand)
        print("Price: ",self.price)
        print("ChargeType: ",self.chargetype)
phone.chargetype="B-TYPE "
oppo=phone("Oppo","15000")
oppo.display()
redmi=phone("Redmi","10000")
redmi.display()
vivo=phone("vivo","5000")
vivo.display()'''

student = {
    "name": "John",
    "age": 21,
    "course": "Python"
}

for value in student.values():
    print(value)
