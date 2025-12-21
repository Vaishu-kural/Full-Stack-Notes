def validate_email(email):
    if "@" in email and "." in email:
        return True
    return False

# Real-time usage
print(validate_email("user@gmail.com"))  # True
#print(validate_email("usergmail.com"))   # False


'''def atm_withdraw(balance, amount):
    if amount <= balance:
        balance -= amount
        print(f"Withdrawal Successful! Remaining Balance: ₹{balance}")
    else:
        print("Insufficient Balance!")
    return balance

# Real-time usage
current_balance = 5000
current_balance = atm_withdraw(current_balance, 2000)'''

'''import random

def generate_otp():
    otp = random.randint(100000, 999999)
    return otp
    #print(otp)

# Real-time usage
print(f"Your OTP is: {generate_otp()}")'''

'''def calculate_total(cart_items):
    total = 0
    for item, price in cart_items.items():
        total += price
    return total

cart = {
    "Laptop": 50000,
    "Headphones": 2000,
    "Mouse": 700
}
print("Total Bill Amount: ₹", calculate_total(cart))
'''

'''def login(username, password):
    if username == "admin" and password == "12345":
        return "Login Successful!"
    else:
        return "Invalid Username or Password!"

# Real-time usage
#print(login("admin", "12345"))
print(login("user", "pass"))'''

'''def book_ticket(movie, seats, price_per_ticket=150):
    total_cost = seats * price_per_ticket
    return f"Movie: {movie}, Total Cost: ₹{total_cost}"

print(book_ticket("KGF 3", 3))'''




