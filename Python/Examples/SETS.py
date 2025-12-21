# Python Set Methods

# Initial Set
fruits = {"apple", "banana"}
print("Initial Set:", fruits)
'''
# 1. add(x)
fruits.add("orange")
print("\nAfter add('orange'):", fruits)

# 2. update([x, y])
fruits.update(["mango", "grape"])
print("After update(['mango', 'grape']):", fruits)

# 3. remove(x)
fruits.remove("banana")
print("After remove('banana'):", fruits)
# fruits.remove("kiwi")  # ❌ Will raise KeyError if uncommented

# 4. discard(x)
fruits.discard("mango")
fruits.discard("kiwi")  # No error if element not found
print("After discard('mango') and discard('kiwi'):", fruits)

# 5. pop()
removed_item = fruits.pop()
print("After pop(), removed:", removed_item)
print("Set after pop():", fruits)

# 6. clear()
temp_set = fruits.copy()
temp_set.clear()
print("After clear():", temp_set)
'''
# 7. union(set)
a = {1, 2, 3}
b = {3, 4, 5}
print("\nUnion of a and b:", a.union(b))

# 8. intersection(set)
print("Intersection of a and b:", a.intersection(b))

# 9. difference(set)
print("Difference of a and b:", a.difference(b))

# 10. symmetric_difference(set)
print("Symmetric Difference of a and b:", a.symmetric_difference(b))
