import os
from getpass import getpass  # For secure password input (optional)

def register_user():
    print("=== User Registration ===")
    name = input("Enter your full name: ")
    email = input("Enter your email: ")
    username = input("Choose a username: ")

    # Masking password input (optional)
    password = getpass("Create a password: ")

    # Check if file exists
    file_path = "registration.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("Name,Email,Username,Password\n")

    # Append user details
    with open(file_path, "a") as f:
        f.write(f"{name},{email},{username},{password}\n")

    print("\nRegistration successful! Your details have been saved.\n")

if __name__ == "__main__":
    register_user()
