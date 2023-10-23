# Import necessary modules
import os
import sys

# Constants should be in UPPERCASE
MAX_ATTEMPTS = 3

# Use a blank line to separate logical sections of code

def greet_user(username):
    """Greet the user by their name."""
    print(f"Hello, {username}!")

# Add two blank lines before function definitions

def get_user_input(prompt):
    """Get user input and return it."""
    user_input = input(prompt)
    return user_input

# Use a blank line to separate logical sections of code

def main():
    """Main function."""
    username = os.getenv("USERNAME")
    
    if not username:
        print("Error: USERNAME environment variable not set.")
        sys.exit(1)
    
    greet_user(username)
    
    for _ in range(MAX_ATTEMPTS):
        user_input = get_user_input("Enter 'Y' to continue or 'N' to exit: ").strip().lower()
        if user_input == 'y':
            print("Continuing...")
        elif user_input == 'n':
            print("Exiting...")
            break
        else:
            print("Invalid input. Try again.")
    else:
        print("Max attempts reached. Exiting...")

if __name__ == "__main__":
    main()
