import re

# Main function
def main():
    while True:
        # Get password from user
        password = input("Enter a password: ")

        # Check if password is secure
        if check_length(password) and check_if_lowercase and check_if_number(password) and check_special_characters(password) and check_if_uppercase(password):
            # If password is secure, print success message
            print("Secure password")
            break
        # If password is not secure, print error message
        else:
            print("Invalid password")

# Check if password is at least 8 characters long
def check_length(password):
    if len(password) >= 8:
        return True

# Check if password contains a number
def check_if_number(password):
    if re.match('^.*[0-9].*$', password):
        return True

# Check if password contains a special character
def check_special_characters(password):
    if re.match('^.*[!@#$%^&*()_+=].*$', password):
        return True

# Check if password contains an uppercase letter
def check_if_uppercase(password):
    if re.match('^.*[A-Z].*$', password):
        return True

# Check if password contains a lowercase letter
def check_if_lowercase(password):
    if re.match('^.*[a-z].*$', password):
        return True

if __name__ == "__main__":
    main()submit50  