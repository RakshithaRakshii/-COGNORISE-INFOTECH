import random
import string

def generate_password(length):
    # Define the character sets for different complexity levels
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets based on user's choice
    all_chars = lowercase + uppercase + digits + symbols

    # Adjust length if it exceeds available characters
    if length > len(all_chars):
        print("Desired length exceeds available characters. Generating password of maximum length...")
        length = len(all_chars)

    # Generate password
    password = ''.join(random.sample(all_chars, length))
    return password

def main():
    print("Password Generator")

    while True:
        length = int(input("Enter the desired length of the password (0 to exit): "))

        if length == 0:
            print("Exiting...")
            break

        if length < 0:
            print("Invalid length! Please enter a positive integer.")
            continue

        password = generate_password(length)
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
