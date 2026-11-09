
import random

# Stores all possible characters used to generate passwords.
characters = [
    "a", "b", "c", "d", "e", "f", "g", "h",
    "i", "j", "k", "l", "m", "n", "o", "p",
    "q", "r", "s", "t", "u", "v", "w", "x",
    "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H",
    "I", "J", "K", "L", "M", "N", "O", "P",
    "Q", "R", "S", "T", "U", "V", "W", "X",
    "Y", "Z",
    "0", "1", "2", "3", "4", "5", "6", "7",
    "8", "9",
    "!", "@", "#", "$", "%", "&", "*"
]


# Generates a random password using the requested length.
def generate_password(password_length):
    password = ""

    # Selects random characters from the list.
    for character_number in range(password_length):
        selected_character = random.choice(characters)
        password = password + selected_character

    return password


# Main function that runs the password generator.
def main():
    print("=== Random Password Generator ===")

    password_length = int(input("How long should your password be? "))

    if password_length <= 0:
        print("Please enter a number greater than 0.")

    else:
        generated_password = generate_password(password_length)

        print("Your random password is:", generated_password)

    print("Thank you for using the generator!")


# Calls the main function to start the program.
main()
