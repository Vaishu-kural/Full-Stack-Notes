# 1) While loop to print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

# 2) For loop to display even numbers between 1 and 20
for num in range(1, 21):
    if num % 2 == 0:
        print(num)

# 3) While loop to calculate the sum of first 10 natural numbers
n = 1
total = 0
while n <= 10:
    total += n
    n += 1
print("Sum of first 10 natural numbers:", total)

# 4) For loop to print each character in the string "Python"
for ch in "Python":
    print(ch)

# 5) Print numbers from 10 to 1 in reverse using a while loop
x = 10
while x >= 1:
    print(x)
    x -= 1

# 6) For loop to calculate the factorial of a given number (example: n = 5)
n = 5
fact = 1
for k in range(1, n + 1):
    fact *= k
print(f"Factorial of {n} is", fact)

# 7) While loop to print squares of numbers from 1 to 5
m = 1
while m <= 5:
    print(m * m)
    m += 1

# 8) Program to check whether a number is prime or not using a for loop (example: n = 29)
n = 29
is_prime = True
if n <= 1:
    is_prime = False
else:
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            is_prime = False
            break
print(n, "is prime:" , is_prime)

# 9) For loop to count vowels in a string
s = "Hello World"
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Vowel count:", count)

# 10) While loop to print only odd numbers from 1 to 20
y = 1
while y <= 20:
    if y % 2 != 0:
        print(y)
    y += 1

# 11) For loop with if condition to print multiplication table of any number (like 7)
num = 7
for i in range(1, 11):
    if i <= 10:
        print(f"{num} x {i} = {num * i}")

# 12) For loop to print the sum of all even numbers between 1 and 50
sum_even = 0
for v in range(1, 51):
    if v % 2 == 0:
        sum_even += v
print("Sum of even numbers 1-50:", sum_even)

# 13) While loop to keep asking the user for a password until it’s correct
correct_password = "secret123"
entered = ""
while entered != correct_password:
    entered = input("Enter password: ")
print("Password accepted")

# 14) For loop to display elements from a list: [10, 20, 30, 40, 50]
lst = [10, 20, 30, 40, 50]
for elem in lst:
    print(elem)

# 15) For loop with break to stop printing numbers once you reach number 7
for n in range(1, 20):
    if n == 7:
        break
    print(n)

# 16) Use continue to skip printing even numbers from 1 to 10
for n in range(1, 11):
    if n % 2 == 0:
        continue
    print(n)

# 17) Create a loop where pass is used when a number is divisible by 3
for n in range(1, 11):
    if n % 3 == 0:
        pass  # placeholder: do nothing for numbers divisible by 3
    else:
        print(n)

# 18) Find the first number divisible by 11 in range 1 to 100 using for and break
result = None
for n in range(1, 101):
    if n % 11 == 0:
        result = n
        break
print("First number divisible by 11 in 1..100:", result)

# 19) While loop with continue to skip numbers divisible by 5 from 1 to 30
i = 1
while i <= 30:
    i += 1
    if i % 5 == 0:
        continue
    if i <= 30:
        print(i)

# 20) Define a for loop with a placeholder using pass to later write logic for checking perfect numbers
for candidate in range(1, 101):
    # TODO: implement perfect number check here
    pass
