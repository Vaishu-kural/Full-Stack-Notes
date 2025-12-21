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


