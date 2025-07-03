#Checking whether the user is child, teenager, adult or senior by taking the input as age

input = int(input("Please Enter the Age:"))

if input <= 12 and input >= 0:
    print("You are a child")

elif input >= 13 and input <= 19:
    print("You are a teenager")

elif input >= 20 and input <= 50:
    print("You are adult")

else:
    print("You are senior")

