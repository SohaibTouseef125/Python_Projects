import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = int(input("Enter the length of the password: "))


if __name__ == "__main__":
    print("Generated Password:", generate_password(password_length))
    
   