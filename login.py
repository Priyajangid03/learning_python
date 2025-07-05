#Simple Login System

username = "priya"
password = "55555"

name = input("Enter username: ")
pin = input("Enter password: ")

if username == name and password == pin:
    print("Login successful! Welcome.")
else:
    print("Invalid username or password.")