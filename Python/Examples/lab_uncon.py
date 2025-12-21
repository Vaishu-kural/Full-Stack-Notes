#6
# Factorial of a number using for loop
'''num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i  # Multiply each number

print(f"The factorial of {num} is: {factorial}")
print("the factorial is",factorial)'''

#8
# Prime number check using for loop
'''num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")'''

#9
# Count vowels in a string using for loop
'''text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"Number of vowels in the string: {count}")'''

