'''try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")'''


'''value = int("abc")'''

'''try:
    value = int("abc")
except ValueError:
    print("Invalid input! Not an integer.")
except TypeError:
    print("Type mismatch!")
'''

'''try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a number!")
else:
    print("You entered:", num)
finally:
    print("This always runs.")'''

class NegativeAgeError(Exception):
    pass

age = -1
if age < 0:
    raise NegativeAgeError("Age cannot be negative")
