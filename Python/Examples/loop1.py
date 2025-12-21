'''def demo():
    print("Hello")
demo()

def add(a,b):
    print(a+b)
add(4,6)
demo()
demo()
demo()'''

'''def greet(name):
    print("Hello", name)
greet("Alice")'''


'''def cube(n):
    return n * n * n
print("Cube:", cube(3))'''

'''def add(a, b):
    return a + b, a - b  # returns a tuple

result = add(5, 3)
print("Sum:", result[0])
print("Difference:", result[1])'''

# def operations(x, y):
#     sum_ = x + y
#     diff = x - y
#     return sum_, diff

# a, b = operations(10, 5)
# print("Sum:", a)
# print("Difference:", b)

#default argument
# def greet(name="Guest"):
#     print("Hello", name)

# greet()        
# greet("Anu")   

'''def student(name, age):
    print(name, "is", age, "years old")

student(age=20, name="Rahul")'''

# def display_info(name, age):
#     print(f"Name: {name}, Age: {age}")

# display_info("Navi", 20)

def add_numbers(*args):
    total = sum(args)
    print("Sum:", total)

add_numbers(2, 3, 5, 7)  # Output: Sum: 17
