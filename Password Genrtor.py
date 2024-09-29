import random
import string

def generate_password(length=6):
    # Define the character set (digits only for a 6-digit password)
    characters = string.digits
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Example usage
if __name__ == "__main__":
    password = generate_password(6)
    print(f"Generated password: {password}")
