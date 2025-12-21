class BankAccount:
    def __init__(self, balance):
        self._balance = balance       # protected
        self.__pin = 1234             # private
    def show_balance(self, pin):
        if pin == self.__pin:
            print("Balance:", self._balance)
        else:
            print("Incorrect PIN!")
account = BankAccount(5000)
account.show_balance(1234)  # Correct PIN
account.show_balance(9999)  # Incorrect PIN
# Direct access
print(account._balance)     # Allowed but not recommended
#print(account.__pin)        # Error: AttributeError
