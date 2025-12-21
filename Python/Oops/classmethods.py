class laptop:
    chargertype="C-Type"        #class variable
    def __init__(self):
        self.brand=""                   #instance variable
        self.price=34
        
    def setPrice(self,price):
        self.price=price
        
    def getPrice(self):             #instance method
        print(self.price)

#    @classmethod                #class method
#    def changeChargerType(cls):
  #      cls.chargertype="B TYPE"
#        print("Charger type changed to B")

#    @staticmethod
 #   def info():
  #      print("This is laptop class")

hp=laptop()
hp.setPrice(20000)          #set into price
hp.getPrice()

#laptop.changeChargerType()          #@class method
#laptop.changeChargerType(laptop) --> one one time class method used this type call

#hp.info()
