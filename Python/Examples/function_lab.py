# ========================================
# PART A: Built-in Functions
# ========================================

# Q1
string = input("Enter a string: ")
print("Length of string:", len(string))

# Q2
a = 10
b = 3.14
c = "Python"
print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))

# Q3
user_name = input("Enter your name: ")
print("Welcome", user_name)

# Q4
numbers = [5, 10, 15, 2, 8]
print("Max:", max(numbers))
print("Min:", min(numbers))

# ========================================
# PART B: User-defined Functions – No Return
# ========================================

# Q5
def greet():
    print("Hello, welcome to Python Functions")
greet()

# Q6
def even_odd(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")
even_odd(7)

# Q7
def display_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
display_table(5)

# Q8
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
countdown(5)

# ========================================
# PART C: User-defined Functions – With Single Return
# ========================================

# Q9
def add(a, b):
    return a + b
print("Sum:", add(4, 5))

# Q10
def cube(n):
    return n ** 3
print("Cube:", cube(3))

# Q11
def is_even(n):
    return n % 2 == 0
print("Is 4 Even?:", is_even(4))

# Q12
def area_circle(r):
    return 3.14 * r * r
print("Area of Circle:", area_circle(5))

# Q13
def max_of_two(a, b):
    return a if a > b else b
print("Max of 10 and 20:", max_of_two(10, 20))

# ========================================
# PART D: Functions Returning Multiple Values
# ========================================

# Q14
def calc(a, b):
    return a + b, a * b
sum_val, product_val = calc(4, 5)
print("Sum:", sum_val, "Product:", product_val)

# Q15
def stats(lst):
    total = sum(lst)
    length = len(lst)
    average = total / length
    return total, length, average
print("Stats:", stats([10, 20, 30, 40]))

# Q16
def rectangle(l, w):
    area = l * w
    perimeter = 2 * (l + w)
    return area, perimeter
print("Rectangle:", rectangle(4, 6))

# Q17
def get_chars(s):
    return s[0], s[-1]
print("First & Last Char:", get_chars("Python"))

# ========================================
# PART E: Advanced
# ========================================

# Q18
def greet_user(name="Guest"):
    print(f"Hello {name}, welcome!")
greet_user()
greet_user("Navi")

# Q19
def user_info(*, name, age):
    print(f"Name: {name}, Age: {age}")
user_info(name="Alice", age=25)

# Q20
def is_palindrome(s):
    return s == s[::-1]
print("Is 'madam' Palindrome?:", is_palindrome("madam"))

# ========================================
# PYTHON FUNCTIONS & SCOPE
# ========================================

# PART A: Positional & Keyword Arguments

# Q1
def student(name, course):
    print(f"Student Name: {name}, Course: {course}")
student("Navi", "Python")

# Q2
def student_kw(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")
student_kw(name="John", age=21, city="New York")

# Q3
def bio(name, age, country):
    print(f"Name: {name}, Age: {age}, Country: {country}")
bio("Alice", age=30, country="India")

# Q4
# Positional after keyword -> ERROR
# bio(name="Alice", 30, country="India")  # Uncomment to see the error

# Q5
def area(length, breadth):
    return length * breadth
print("Area (Positional):", area(5, 6))
print("Area (Keyword):", area(length=7, breadth=8))

# ========================================
# PART B: Default Arguments
# ========================================

# Q6
def greet_default(name="Guest"):
    print(f"Hello {name}")
greet_default()
greet_default("Navi")

# Q7
def power(base, exponent=2):
    return base ** exponent
print("Power:", power(3))
print("Power:", power(2, 3))

# Q8
def ticket(name, price=100):
    print(f"Ticket for {name}, Price: {price}")
ticket("Alice")
ticket("Bob", 150)

# Q9
def login(user="admin", pwd="1234"):
    print(f"User: {user}, Password: {pwd}")
login()
login("Navi", "abcd")

# ========================================
# PART C: *args and **kwargs
# ========================================

# Q10
def sum_all(*nums):
    return sum(nums)
print("Sum of All:", sum_all(1, 2, 3, 4))

# Q11
def average(*nums):
    return sum(nums) / len(nums)
print("Average:", average(10, 20, 30))

# Q12
def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
info(name="Navi", age=21, branch="CSE")

# Q13
def square_each(*args):
    for num in args:
        print(f"Square of {num} is {num ** 2}")
square_each(2, 3, 4)

# Q14
def combine(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)
combine(1, 2, 3, name="Alice", age=25)

# ========================================
# PART D: Scope of Variables
# ========================================

# Q15
def local_var_demo():
    x = 10
    print("Inside Function:", x)
local_var_demo()
# print(x)  # ❌ Error: x is not defined outside function

# Q16
global_var = 50
def show_global():
    print("Global Variable:", global_var)
show_global()

# Q17
count = 0
def modify_global():
    global count
    count += 1
    print("Updated Global Count:", count)
modify_global()

# Q18
def outer():
    outer_var = "I am outer"
    def inner():
        print("Inner can access:", outer_var)
    inner()
outer()

# Q19
def outer_nonlocal():
    value = "Original"
    def inner():
        nonlocal value
        value = "Updated"
        print("Inner Value:", value)
    inner()
    print("Outer Value after update:", value)
outer_nonlocal()

# Q20
x = 100
def demo_scope():
    x = 50
    print("Local x:", x)
demo_scope()
print("Global x:", x)
