'''fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)'''

#add items in set
'''colors = {"red", "blue"}
colors.add("green")              # Add one item
colors.update(["yellow", "pink"])  # Add multiple
print(colors)'''

#delete items in set
'''colors = {"red", "green", "blue"}
print(type(colors))
#colors.remove("green")
#colors.discard("purple")  # No error
#colors.pop()
colors.clear()
print(colors)'''

#loop
'''numbers = {10, 20, 30, 40}
for num in numbers:
    print(num)'''

a = {"apple", "banana"}
b = {"cherry", "banana"}

# Union (new set)
'''c = a.union(b)
print(c)'''

'''# Update (modify a)
a.update(b)
print(a)

my_set = {3, 1, 4, 2}
sorted_list = sorted(my_set)
print(sorted_list)  # Output: [1, 2, 3, 4]'''


nums=(10,20,30,40,50)
print(nums[2])
print(nums[:-4:-1])

