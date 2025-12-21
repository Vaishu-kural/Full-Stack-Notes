# def q1_positive():
#     n = int(input("Enter a number: "))
#     if n > 0:
#         print("Positive")
#     else:
#         print("Not Positive")

# def q2_even_odd():
#     n = int(input("Enter a number: "))
#     if n % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# def q3_pos_neg_zero():
#     n = int(input("Enter a number: "))
#     if n > 0:
#         print("Positive")
#     elif n < 0:
#         print("Negative")
#     else:
#         print("Zero")

# def q4_vote():
#     age = int(input("Enter age: "))
#     print("Eligible to vote" if age >= 18 else "Not eligible to vote")

# def q5_pass_fail():
#     marks = float(input("Enter marks: "))
#     print("Pass" if marks >= 40 else "Fail")

# def q6_vowel_consonant():
#     ch = input("Enter a character: ").lower()
#     if ch in "aeiou":
#         print("Vowel")
#     else:
#         print("Consonant")

# def q7_largest_two():
#     a, b = map(int, input("Enter two numbers: ").split())
#     print("Largest:", a if a > b else b)

# def q8_largest_three():
#     a, b, c = map(int, input("Enter three numbers: ").split())
#     if a >= b and a >= c:
#         print("Largest:", a)
#     elif b >= c:
#         print("Largest:", b)
#     else:
#         print("Largest:", c)

# def q9_classify_temp():
#     temp = float(input("Enter temperature: "))
#     if temp > 30:
#         print("Hot")
#     elif 20 <= temp <= 30:
#         print("Warm")
#     else:
#         print("Cold")

# def q10_grade_score():
#     score = int(input("Enter score: "))
#     if score >= 90:
#         grade = "A"
#     elif score >= 80:
#         grade = "B"
#     elif score >= 70:
#         grade = "C"
#     elif score >= 60:
#         grade = "D"
#     else:
#         grade = "F"
#     print("Grade:", grade)

# def q11_leap_year():
#     year = int(input("Enter year: "))
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print("Leap Year")
#     else:
#         print("Not a Leap Year")

# def q12_divisible_3_5():
#     n = int(input("Enter number: "))
#     if n % 3 == 0 and n % 5 == 0:
#         print("Divisible by 3 and 5")
#     else:
#         print("Not divisible by 3 and 5")

# def q13_even_odd_zero():
#     n = int(input("Enter number: "))
#     if n == 0:
#         print("Zero")
#     elif n % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# def q14_char_classify():
#     ch = input("Enter a character: ")
#     if ch.isupper():
#         print("Uppercase")
#     elif ch.islower():
#         print("Lowercase")
#     elif ch.isdigit():
#         print("Digit")
#     else:
#         print("Special Character")

# def q15_marks_5():
#     marks = list(map(float, input("Enter marks of 5 subjects separated by space: ").split()))
#     total = sum(marks)
#     avg = total / 5
#     print("Total:", total)
#     print("Average:", avg)
#     if avg >= 90:
#         grade = "A"
#     elif avg >= 80:
#         grade = "B"
#     elif avg >= 70:
#         grade = "C"
#     elif avg >= 60:
#         grade = "D"
#     else:
#         grade = "F"
#     print("Grade:", grade)

# def q16_password():
#     correct = "abc123"
#     pwd = input("Enter password: ")
#     print("Access Granted" if pwd == correct else "Invalid Password")

# def q17_positive_div5():
#     n = int(input("Enter number: "))
#     if n > 0 and n % 5 == 0:
#         print("Positive and divisible by 5")
#     else:
#         print("Condition not met")

# def q18_atm_pin():
#     pin = 1234
#     entered = int(input("Enter PIN: "))
#     print("Access Granted" if entered == pin else "Incorrect PIN")

# def q19_triangle_type():
#     a, b, c = map(float, input("Enter three sides: ").split())
#     if a == b == c:
#         print("Equilateral")
#     elif a == b or b == c or a == c:
#         print("Isosceles")
#     else:
#         print("Scalene")

# def q20_calculator():
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     op = input("Enter operation (+, -, *, /): ")
#     if op == "+":
#         print("Result:", a + b)
#     elif op == "-":
#         print("Result:", a - b)
#     elif op == "*":
#         print("Result:", a * b)
#     elif op == "/":
#         print("Result:", a / b if b != 0 else "Division by zero error")
#     else:
#         print("Invalid operator")

# # Menu
# options = [
#     q1_positive, q2_even_odd, q3_pos_neg_zero, q4_vote, q5_pass_fail,
#     q6_vowel_consonant, q7_largest_two, q8_largest_three, q9_classify_temp,
#     q10_grade_score, q11_leap_year, q12_divisible_3_5, q13_even_odd_zero,
#     q14_char_classify, q15_marks_5, q16_password, q17_positive_div5,
#     q18_atm_pin, q19_triangle_type, q20_calculator
# ]

# while True:
#     print("\nChoose a program to run:")
#     for i, func in enumerate(options, 1):
#         print(f"{i}. {func.__name__}")
#     print("0. Exit")
#     choice = int(input("Enter your choice: "))
#     if choice == 0:
#         break
#     elif 1 <= choice <= len(options):
#         options[choice-1]()
#     else:
#         print("Invalid choice!")

t1 = (2,3,4,5,6,7)
if t1 % 2 ==0:
    print(t1)