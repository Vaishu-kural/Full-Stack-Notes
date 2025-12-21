def add(a=10):
    print(a)
add(56)
#normal function
def add(a,b):
    print(a+b)
add(2,3)

#3 arg/parameter
def add(a,b,c):
    print(a+b+c)
add(2,3,9)
#(2,3,4)


#3 arg/parameter(polymorphism)
def add(a,b,c=0):
    print(a+b+c)
add(2,3)
add(1,2,4)

