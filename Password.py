import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


while True:
    try:
        password_length = int(input("Enter the desired password length: "))
        if password_length <= 0:
            print("Password length must be greater than 0.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer length.")

generated_password = generate_random_password(password_length)
print(f"Generated Password: {generated_password}")

