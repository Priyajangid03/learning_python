#Time of day greeting

time = int(input("Enter the time: "))

if time < 0 or time > 23:
    print("Invalid time.")
elif time < 5:
    print("Good Night!")
elif time < 12:
    print("Good Morning!")
elif time < 17:
    print("Good Afternoon!")
elif time < 21:
    print("Good Evening!")
else:
    print("Good Night!")