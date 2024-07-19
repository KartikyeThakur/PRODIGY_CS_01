def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            char_code = ord(char) - ascii_offset
            shifted_code = (char_code + shift) % 26
            encrypted_char = chr(shifted_code + ascii_offset)
            result += encrypted_char
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            char_code = ord(char) - ascii_offset
            shifted_code = (char_code - shift) % 26
            decrypted_char = chr(shifted_code + ascii_offset)
            result += decrypted_char
        else:
            result += char
    return result

def main():
    while True:
        print("\nCaesar Cipher Program")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            text = input("Enter a message to encrypt: ")
            while True:
                try:
                    shift = int(input("Enter a shift value (1-25): "))
                    if 1 <= shift <= 25:
                        break
                    else:
                        print("Invalid shift value. Please enter a value between 1 and 25.")
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            encrypted_text = caesar_encrypt(text, shift)
            print(f"\nEncrypted message: {encrypted_text}")
        elif choice == "2":
            text = input("Enter a message to decrypt: ")
            while True:
                try:
                    shift = int(input("Enter a shift value (1-25): "))
                    if 1 <= shift <= 25:
                        break
                    else:
                        print("Invalid shift value. Please enter a value between 1 and 25.")
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            decrypted_text = caesar_decrypt(text, shift)
            print(f"\nDecrypted message: {decrypted_text}")
        elif choice == "3":
            break
        else:1
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
