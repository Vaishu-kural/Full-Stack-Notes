'''try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
'''
'''try:
    a=4
    b=int(input("b:"))
    c=a/b 
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(c)
finally:
    print("Runs")

try:
    value = int("abc")
except ValueError:
    print("Invalid input! Not an integer.")
except TypeError:
    print("Type mismatch!")
'''
'''try:
    value = 2
    #b=int("abc")   #valueerror
    b="abd" #typeerror
    c=value+b
except ValueError:
    print("Invalid input! Not an integer.")
except TypeError:
    print("Type mismatch!")'''

'''try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a number!")
else:
    print("You entered:", num)
finally:
    print("This always runs.")'''

try:
    x = "10" + 5
except Exception as e:
    print("Error occurred:", e)

x = "10" + 5
print(x)

'''class NegativeAgeError(Exception):
    pass
age = -1
if age < 0:
    raise NegativeAgeError("Age cannot be negative")'''

'''try:
    with open("nonexistent.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found!")
'''
