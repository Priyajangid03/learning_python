#checking the divisibilty by both 4 and 6 by taking the user input

input = int(input("Please enter the number: "))
if input % 4 == 0 and input % 6 == 0:
    print("The number is divisible by both 4 & 6")
else:
    print("The entered number is not divisible by both")