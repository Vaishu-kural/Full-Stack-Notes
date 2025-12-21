# 1. Handle division by zero using try-except
print("\n1. Division by Zero Handling")
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# 2. Handle invalid integer input
print("\n2. Handle Invalid Integer Input")
try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except ValueError:
    print("Error: That’s not a valid number!")

# 3. Handle file not found error
print("\n3. Handle File Not Found")
try:
    f = open("nonexistent.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Error: File not found!")

# 4. Handle multiple exceptions
print("\n4. Handle Multiple Exceptions")
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
    print("Result:", result)
except ValueError:
    print("Error: Please enter valid numbers only.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# 5. Use finally block
print("\n5. Demonstrate Finally Block")
try:
    n = int(input("Enter a number: "))
    print("Square:", n * n)
except:
    print("Something went wrong.")
finally:
    print("This block always runs.")

# 6. Raise custom exception for negative number
print("\n6. Raise Custom Exception")
try:
    n = int(input("Enter a positive number: "))
    if n < 0:
        raise ValueError("Negative numbers not allowed!")
    print("You entered:", n)
except ValueError as e:
    print("Error:", e)

# 7. Handle IndexError
print("\n7. Handle IndexError in List")
try:
    nums = [10, 20, 30]
    print("List:", nums)
    index = int(input("Enter index to access: "))
    print("Value:", nums[index])
except IndexError:
    print("Error: Invalid index!")

# 8. Demonstrate else block with try-except
print("\n8. Demonstrate Else Block")
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print("You entered a valid number:", num)


# 9. Create a new text file and write content
print("\n9. Create and Write File")
with open("example.txt", "w") as f:
    f.write("Hello, this is a new file.\nWelcome to Python file handling!\n")
print("File 'example.txt' created and written successfully.")

# 10. Read and display the contents of a text file
print("\n10. Read and Display File Content")
try:
    with open("example.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: File not found!")

# 11. Append new content to existing file
print("\n11. Append New Content")
with open("example.txt", "a") as f:
    f.write("This line was appended successfully.\n")
print("New content appended.")

# 12. Count number of lines in a file
print("\n12. Count Lines in File")
with open("example.txt", "r") as f:
    lines = f.readlines()
    print("Total lines:", len(lines))

# 13. Print only lines containing 'Python'
print("\n13. Print Lines Containing 'Python'")
with open("example.txt", "r") as f:
    for line in f:
        if "Python" in line:
            print(line.strip())

# 14. Copy contents from one file to another
print("\n14. Copy File Content")
with open("example.txt", "r") as src, open("copy_example.txt", "w") as dest:
    dest.write(src.read())
print("Content copied to 'copy_example.txt'.")

# 15. Handle file errors safely
print("\n15. Handle File Errors Safely")
try:
    with open("nofile.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: File does not exist.")
