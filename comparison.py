#comparing two numbers

input1 = int(input("Enter the first number: "))
input2 = int(input("Enter the second number: "))

if input1 > input2:
    print("The first number is greater.")
elif input2 > input1:
    print("The second number is greater.")
else:
    print("Both numbers are equal.")