class laptop:
    chargertype="C-Type"        #class variable
    def __init__(self):
        self.brand=""                   #instance variable
        self.price=34
        
    def setPrice(self,price):
        self.price=price
        
    def getPrice(self):             #instance method
        print(self.price)

    @classmethod
    def changeChargerType(cls):         #class method
        cls.chargertype="B TYPE"
        print("Charger type changed to B")

    @staticmethod
    def info():
        print("This is laptop class")


acer=laptop()
acer.setPrice(20000)
acer.getPrice()

asus=laptop()
asus.getPrice()

laptop.changeChargerType()
acer.info()
