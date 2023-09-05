import random

character="abcdefghijklmnopqrstuvwxyz0123456789@#$%&_*"

# password length user input
passlen=int(input("Enter the length of the password"))

password=""
for i in range(0,passlen):
    pass_char=random.choice(character)
    password+=pass_char
print("your password is",password)