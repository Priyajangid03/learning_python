#checking days in a month

input = int(input("Enter month: "))

if input == 2:
    print("There are 28 days in this month")
elif input in [1, 3, 5, 7, 8, 10, 12]:
    print("There are 31 days in this month")
elif input in [4, 6, 9, 11]:
    print("There are  days in this month")
else:
    print("Invalid month")