#create and write
file = open("ex.txt", "w")
file.write("Hello, Python!\n")
file.write("This is a file write example.")
file.close()

#Read from a File ('r' mode)
file = open("ex.txt", "r")
content = file.read()
print(content)
file.close()

#Append to a File ('a' mode)
file = open("ex.txt", "a")
file.write("\nNew line added.")
file.close()

#Read line by line
file = open("ex.txt", "r")
for line in file:
    print(line)  # Adds an extra newline because `line` already ends with `\n`
    print(line.strip())  # Removes the existing `\n`, so only one line is printed cleanly.
file.close()

#Using with Statement
with open("ex.txt", "r") as file:
    data = file.read()
    print(data)
