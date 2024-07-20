import re
import secrets
import string

def generate_password(length, nums, special_chars, uppercase, lowercase):
    # Define the possible characters for each category
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Check if length is sufficient to include all required characters
    if length < (nums + special_chars + uppercase + lowercase):
        raise ValueError("Password length is too short to meet the specified requirements.")

    # Ensure that the password will include at least the required number of each type
    password = []
    password.extend(secrets.choice(digits) for _ in range(nums))
    password.extend(secrets.choice(symbols) for _ in range(special_chars))
    password.extend(secrets.choice(string.ascii_uppercase) for _ in range(uppercase))
    password.extend(secrets.choice(string.ascii_lowercase) for _ in range(lowercase))

    # Fill the remaining length with random choices from all categories
    all_characters = letters + digits + symbols
    remaining_length = length - len(password)
    password.extend(secrets.choice(all_characters) for _ in range(remaining_length))

    # Shuffle the password to ensure randomness
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

def get_user_input():
    try:
        length = int(input("Enter the total length of the password: "))
        nums = int(input("Enter the minimum number of digits required: "))
        special_chars = int(input("Enter the minimum number of special characters required: "))
        uppercase = int(input("Enter the minimum number of uppercase letters required: "))
        lowercase = int(input("Enter the minimum number of lowercase letters required: "))

        # Generate and print the password
        new_password = generate_password(length, nums, special_chars, uppercase, lowercase)
        print('Generated password:', new_password)
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    get_user_input()
