#Taking color as a input and giving instructions
input = input("Enter the traffic light color: ")

if input == "red":
    print("Stop!")
elif input == "yellow":
    print("Slow down and stop.")
elif input == "green":
    print("Go!.")
else:
    print("Please enter a valid color.")