class phone():
    def __init__(self,brand,price,chargetype):
        self.brand=brand
        self.price=price
        self.chargetype=chargetype
    def display(self):
        print("\nBrand: ",self.brand)
        print("Price: ",self.price)
        print("ChargeType: ",self.chargetype)

oppo=phone("Oppo","15000","C-TYPE")
oppo.display()

redmi=phone("Redmi","10000","C-TYPE")
redmi.display()
