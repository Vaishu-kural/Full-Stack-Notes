
'''print(student)
#Access values in dictionary
print(student["name"])
print(student["age"])
print(student["age"],student["course"])'''

#new value
'''student["city"] = "Chennai"
print(student)'''
#update
'''student["age"]=22
print(student)'''
#delete
'''del student["course"]
print(student)'''

'''print(student["dept"])  
print(student.get("dept"))'''

#remove - pop()
'''student.pop("age")
print(student)
student.popitem()
print(student)

student.clear()
print(student)'''
print(student)
#looping
'''for key in student:
    print(key)



for key, value in student.items():
    print(key, ":",value)'''

#copy()
'''new_dict = student.copy()
print(new_dict)
'''
#nested dictionary
# students = {
#     "student1": {
#         "name": "Alice",
#         "age": 20
#     },
#     "student2": {
#         "name": "Bob",
#         "age": 22
#     }
# }
# print(students["student1"]["name"])

#dict-sort-values
'''data = {'banana': 3, 'apple': 5, 'cherry': 2}
sorted_by_value = dict(sorted(data.items(), key=lambda item: item[1]))
print(sorted_by_value)
# Output: {'cherry': 2, 'banana': 3, 'apple': 5}'''

#dict-sort-in-keys
'''data = {'banana': 3, 'apple': 5, 'cherry': 2}
sorted_by_key = dict(sorted(data.items()))
print(sorted_by_key)'''

