import random
import string

def generate_password(length):
    # Define character sets for password complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on complexity
    if length < 4:
        print("Password length must be at least 4 characters.")
        return
    elif length < 8:
        charset = lowercase_letters + digits
    elif length < 12:
        charset = lowercase_letters + uppercase_letters + digits
    else:
        charset = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate the password
    password = ''.join(random.choice(charset) for _ in range(length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")

if __name__ == "__main__":
   main()