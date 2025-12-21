'''i = 1
while i <= 5:
    print(i)
    i += 1'''
'''
i=i+1
1+1=2
2+1=3
3+1=4
4+1=5
'''
'''pin = 1234
user_pin = int(input("Enter your ATM PIN: "))
attempts = 1
while user_pin != pin and attempts < 3:
    print("Incorrect PIN! Try again.")
    user_pin = int(input("Enter your ATM PIN: "))
    attempts += 1

if user_pin == pin:
    print("Access Granted. Welcome!")
else:
    print("Card Blocked! Too many wrong attempts.")'''

'''while True:
    name = input("Enter your name (type 'exit' to quit): ")
    if name.lower() == "exit":
        print("Program ended!")
        break
    print(f"Hello, {name}!")'''

'''num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        #continue
        #pass
        break
    print(num)'''

'''for i in range(1, 10):
    print(i)'''

for i in range(1, 10):
    if i == 5:
        pass
    
    print(i)






