import pikepdf
from termcolor import colored

# Open the password file using a context manager
with open("C:/Users/USER/OneDrive/Desktop/html/InlighnTech/six_digit_numbers.txt") as file:
    for password in file:
        password = password.strip()  # Strip whitespace/newline characters
        try:
            # Attempt to open the PDF file with the current password
            with pikepdf.open("C:/Users/USER/OneDrive/Desktop/html/InlighnTech/protected_example2.pdf", password=password) as pdf:
                print(colored("Password Found: {}".format(password), 'green'))
                break  # Exit the loop if the password is found
        except pikepdf.PasswordError:
            print(colored("Trying password: {}".format(password), 'red'))
            continue  # Continue to the next password
        except Exception as e:
            print(colored("An error occurred: {}".format(e), 'yellow'))
            break  # Exit on unexpected errors

