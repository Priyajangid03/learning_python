#taking input as a character from user and checking whether it is a vowel or consonent 

input = input("Enter a single letter: ")

if input in 'aeiou' or input in 'AEIOU':
    print("It is a vowel.")
else:
    print("It is a consonant.")