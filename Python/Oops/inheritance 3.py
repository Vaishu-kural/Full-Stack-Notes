#Multilevel Inheritance
class grandpa():
    def phone(self):
        print("grandpa's phone")

class dad(grandpa):                    #class dad(grandpa):
    def money(self):
        print("dad's money")

class son(dad):                    #class son(dad):
    def laptop(self):
        print("son's laptop")

ram = son()
#ram.laptop()
#ram.money()

#d1=dad()
#d1.phone()

ram.phone()     # ==> multilevel inheritance
