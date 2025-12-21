#default  arg
'''def greet(name, city="Bangalore"):
    print(f"Hello {name} from {city}")

greet("aditi")           # Uses default city
greet("Rahul", "Delhi") '''

#positional arg
'''def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
greet("Alice", 25)
greet(67,"abc")'''

#keyword arg
'''def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet(age=30, name="Bob")'''

#variable length arg
'''def add(*number):
    total = sum(number)
    print("Sum is", total)
add(1)
add(10, 20,78,98)'''

''''def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
student_info(name="Kiran", age=21, course="Python")'''

'''def order_summary(order_id, *items, **customer_info):
    print("Order ID:", order_id)
    print("Items Ordered:", items)
    print("Customer Info:", customer_info)

order_summary(101, "Laptop", "Mouse", name="John", address="USA")'''

'''x=7
def demo():
    x=67
    print(x)
    print(x)
demo()'''

'''message="hii"
def greet():
    message = "Hello"
    print(message)
greet()
print(message)'''

'''x = 5
def modify():
    global x
    x = 10
modify()
print("Updated x:", x)'''

def outer():
    x = "Python"
    def inner():
        nonlocal x
        x = "Java"
    inner()
    print("Value of x:", x)
#outer()











