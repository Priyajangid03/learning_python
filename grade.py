#Checking the students Grade

input = int(input("Enter the Score: "))

if input <= 30:
    print("It's F Grade")

elif input >= 31 and input <= 50:
    print("It's D Grade")

elif input >= 51 and input <= 60:
    print("It's C Grade")

elif input >= 61 and input <= 80:
    print("It's B Grade")

elif input >= 81 and input <= 90:
    print("It's A Grade")

elif input >= 91 and input <= 100:
    print("It's A+ Grade")
