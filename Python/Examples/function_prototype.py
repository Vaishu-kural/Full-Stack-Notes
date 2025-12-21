#default and with run time value
#1.fn w/o arg
'''def add():
    a=5
    b=10
    c=a+b
    print(c)
add()'''
#1.fn w/o return type
'''def add():
    a=int(input("a value:"))
    b=int(input("b value"))
    c=a+b
    d=a-b
    print(c)
    #print(d)
add()
#add()'''

#2.fn with arg and without return type(default)
'''def add(a,b):
    c=a+b
    print(c)
add(3,5)'''

#2.with arg and runtime value
'''def add(a,b):
    c=a+b
    print(c)
a1=int(input("enter a value:"))
b1=int(input("enter b value:"))
add(a1,b1)'''

#3.fn w/o arg and with return type
'''def add():
    a=5
    b=10
    c=a+b
    return c
print(add())'''

#3.fn runtime value
'''def add():
    a=int(input("enter a value:"))
    b=int(input("enter b value:"))
    c=a+b
    return c
print(add())'''

#4. fn with arg and with return type - default value
'''def add(a,b):
    c=a+b
    return c
print(add(4,5))'''

#4.fn with arg and with return type - run time
'''def add(a,b):
    c=a+b
    return c
a1=int(input("enter a value:"))
b1=int(input("enter b value:"))
print(add(a1,b1))'''


