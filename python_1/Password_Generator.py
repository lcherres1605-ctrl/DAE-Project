
import random

print("=== Random Password Generator ===")

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"

length = int(input("How long should your password be? "))

password = ""

if length <= 0:
    print("Please enter a number greater than 0.")

else:
    for i in range(length):
        password = password + random.choice(characters)

    print("Your random password is:", password)

print("Thank you for using the generator!")
