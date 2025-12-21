# def countdown(n):
#     while n > 0:
#         print(n)
#         n -= 1
# countdown(5)

# variable-length function => 1. Arbitary Positional(*args), 2. Arbitary Keyword(**kwargs)

# def add(*numbers):
#     total = sum(numbers)
#     print("Sum is", total)

# add(1, 2, 3)
# add(10, 20)
# add(1,2,3,4,5)

# def student_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# student_info(name="Kiran", age=21, course="Python")

#local scope

# def greet():
#     message = "Hello"
#     print(message)
# greet()
# print(message)

# x = 100  # Global variable
# def show():
#     x = 90
#     print("Inside function:", x)
#     print(x)
# show()
# print("Outside function:", x)
# print(x)

# x = 5
# def modify():
#     global x
#     x = 10
# modify()
# print("Updated x:", x)

# def outer():
#     x = "Python"
#     def inner():
#         nonlocal x
#         x = "Java"
#     inner()
#     print("Value of x:", x)
# outer()


# def mix_example(a, b, *args, c=10, **kwargs):
#     print("a:", a)
#     print("b:", b)
#     print("args:", args)
#     print("c:", c)
#     print("kwargs:", kwargs)

# print(mix_example(1, 2, 3, 4, 5, c=15, name="Alice", age=25))

# s = (1,2,3,4)
# for i in s:
#     print(i)
# if i%2==0:
#     print(i)
# #         print("Odd")

values = (4, 5, 6, 7)

print(values[::-1])

