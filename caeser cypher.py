def caesar_cypher(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) %26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) %26 + 97)
        else:
            result += char
    return result
def main():
    text = input("Enter the text to encrypt: ")
    
    # Use try-except to handle invalid input for shift
    try:
        shift = int(input("Enter the shift value (1-25): ").strip())
    except ValueError:
        print("Please enter a valid integer for the shift value.")
        return
    
    # Ensure the shift is within the range
    if shift < 1 or shift > 25:
        print("Shift value must be between 1 and 25.")
        return

    encrypted_text = caesar_cipher(text, shift)
    print("Encrypted text:", encrypted_text)
