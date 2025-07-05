#checking whether a character is in lowercase or uppercase

char = input("Enter a character: ")

if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    print("It is an uppercase letter.")
elif char in 'abcdefghijklmnopqrstuvwxyz':
    print("It is a lowercase letter.")
else:
    print("It is not a character.")