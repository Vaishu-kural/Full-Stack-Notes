#public, class and protected acces specifier

 #normal  => public
# class company():
#     def __init__(self):
#         self.companyName="Google"

# c1=company()
# c1.companyName="Gooooogle"
# print(c1.companyName)

#2 error
# class company():
#     def __init__(self):
#         self.__companyName="Google"

#     def show(self):
#         print(self.__companyName)
# c1=company()
# c1.show()
# print(c1.__companyName)

#private variables class access within the class
# class company:
#     def __init__(self):
#         self.__name="Google"
#     def show(self):
#         print(self.__name)
# p = company()
# p.show()
#Cannot access directly (Encapsulated)

#3 protected --- inherit the class
class company():
    def __init__(self):
        self._companyName="Google"

class b(company):
    pass
b1=b()
print(b1._companyName)
