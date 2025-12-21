
'''my_tuple = ("apple", "banana", "cherry")
print(type(my_tuple))
print(my_tuple[1])      # Output: banana
print(my_tuple[-1]) '''

#tuple to list and list to tuple
'''my_tuple = ("apple", "banana", "cherry")
temp_list = list(my_tuple)
print(type(temp_list))
temp_list[1] = "orange"
my_tuple = tuple(temp_list)
print(my_tuple)
#print(temp_list)'''

#Unpacking a list
'''fruits = ("apple", "banana", "cherry")
print(fruits)
a, b, c = fruits
print(a)   # Output: apple
print(c)   # Output: cherry'''

#arbitary *(asterisk)
'''fruits = ("apple", "banana", "cherry", "mango",'iuyiu')
a,c,*b = fruits
print(a)   # apple
print(b)   # ['banana', 'cherry', 'mango']'''

#loop
'''my_tuple = ("apple", "banana", "cherry")
number=(1,2,3,4)

for item in my_tuple:
    print(item)
#or
for a in range(len(number)):
    print(number[a])
    
for i in range(len(my_tuple)):
    print(my_tuple[i])

#print(len(my_tuple))
'''
#Join
'''tuple1 = (1, 2, 3)
tuple2 = (4, 5)
result = tuple1 + tuple2
print(result)

fruits = ("apple", "banana")
result = fruits * 2
print(result)

num=(1,2,3,4,5)
c=num*2
print(c)'''

#count
'''t = (1, 2, 3, 1, 1)
print(t.count(1))
'''

#index
t = (1, 2, 3, 4)
print(t.index(3))

