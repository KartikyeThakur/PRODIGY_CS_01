# PRODIGY_CS_01
The Caesar Cipher is a classic encryption algorithm used to encode and decode text by shifting characters in the alphabet.This command-line application built in Python provides functionality for both encrypting and decrypting messages using the Caesar Cipher technique. Users can input a message and specify a shift value to perform the encryption or decryption.
 

## Project Title
## Caesar Cipher

## Description
The Caesar Cipher is one of the simplest and most well-known encryption techniques, used for encoding and decoding text by shifting characters in the alphabet. Named after Julius Caesar, who used it to protect his messages, this encryption method involves substituting each letter in the plaintext with a letter found by moving a fixed number of places down or up the alphabet.

This project is a command-line application written in Python that allows users to perform both encryption and decryption using the Caesar Cipher algorithm. The program accepts a message and a shift value as inputs from the user:

- **Encryption**: The user inputs a plaintext message and a shift value. The program shifts each letter of the message by the specified number of positions in the alphabet, resulting in an encrypted ciphertext. Non-alphabetic characters, such as spaces and punctuation, remain unchanged.
  
- **Decryption**: To retrieve the original message, the user inputs the encrypted message along with the same shift value used during encryption. The program reverses the shifting process to decode the ciphertext back into plaintext.

### Key Features:
1. **Shift Value Flexibility**: Users can specify any integer shift value between 1 and 25, allowing for a wide range of encryption possibilities. Shift values outside this range are not accepted, ensuring valid and manageable transformations.

2. **Detailed Debug Information**: For educational and debugging purposes, the program provides detailed output showing the shift values and intermediate character transformations. This helps users understand how each character is processed during encryption and decryption.

3. **Command-Line Interface**: The program operates through a simple command-line interface, making it easy to use and accessible without the need for a graphical user interface (GUI).

4. **Input Validation**: Includes validation to ensure the shift value is numeric and falls within the accepted range. This prevents errors and ensures the program operates correctly.

5. **Non-Alphabetic Characters**: The Caesar Cipher implementation handles non-alphabetic characters gracefully, preserving them in the output without modification. This ensures that spaces, punctuation, and other symbols are not affected by the encryption or decryption processes.

The Caesar Cipher program provides a hands-on way to explore basic encryption techniques and understand their applications. Whether used for educational purposes or simple text manipulation, this tool demonstrates fundamental principles of cryptography in a clear and practical manner.

## API Reference
This project does not utilize any external APIs. All functionalities are implemented using Python's standard libraries.

## Color Reference
This project does not include a graphical user interface (GUI) or color references, as it operates in a command-line environment.

## Features
- **Encryption and Decryption**: Users can encrypt and decrypt messages using the Caesar Cipher by specifying a shift value.
- **Debug Information**: Detailed debug output showing the shift values and intermediate steps for each character during the encryption and decryption processes.
- **Input Validation**: Ensures the shift value is within the valid range (1-25) and handles non-numeric input gracefully.

## Modules Used
- **Standard Libraries**: Python's built-in libraries `ord`, `chr`, and `print` for character manipulation and console output.

## Environment Variables
This project does not require any specific environment variables.

## Demo
Include screenshots or gifs demonstrating the application's functionality. 
![Screenshot (112)](https://github.com/user-attachments/assets/11224360-76c2-4b00-8a52-79649cb203df)


## Installation
To run the Caesar Cipher program locally, ensure you have Python installed on your system. No additional modules are required beyond Python's standard library.

## Lessons Learned
- **Encryption Algorithms**: Gained a deeper understanding of classical encryption techniques and their implementation.
- **Command-Line Applications**: Improved skills in creating and managing command-line applications in Python.
- **Debugging**: Enhanced debugging skills by adding detailed output for each step in the encryption and decryption processes.

## Optimizations
Future enhancements for the Caesar Cipher program could include:
- **GUI Integration**: Adding a graphical user interface for more user-friendly interactions.
- **Advanced Encryption**: Implementing additional encryption algorithms for more robust security options.
- **User Preferences**: Allowing users to save and load their preferred shift values.

## Run Locally
To run the Caesar Cipher program locally, execute the following command:

```bash
python caesar_cipher.py
```

## Running Tests
This project does not currently include automated tests. Manual testing has been conducted to ensure the functionality and correctness of the encryption and decryption processes.

## Usage/Examples
After running the application:
1. Choose whether to encrypt or decrypt a message.
2. Enter the message you wish to process.
3. Provide the shift value (an integer between 1 and 25).
4. View the result and detailed debug information about each character's transformation.

## Sample Output
![Screenshot (121)](https://github.com/user-attachments/assets/d003d3bc-267f-4603-8152-fe8d6e7db07e)
![Screenshot (120)](https://github.com/user-attachments/assets/4fbb6e75-9476-4ae4-9cd3-1aeb384027f9)
![Screenshot (119)](https://github.com/user-attachments/assets/57817e89-c72c-4dcb-81bd-a5ae0f8f59d8)
![Screenshot (118)](https://github.com/user-attachments/assets/ec2bcbed-19a1-459a-88be-6d47e3e589aa)
![Screenshot (117)](https://github.com/user-attachments/assets/9bc3951e-4dee-4455-abb9-8df62f71070e)
![Screenshot (116)](https://github.com/user-attachments/assets/a5b7842f-6422-4b79-a07b-bc214658f2bc)
![Screenshot (115)](https://github.com/user-attachments/assets/e04ed078-e089-412b-a29b-2591bdb1b212)
![Screenshot (114)](https://github.com/user-attachments/assets/b1802b02-d3bf-46f3-8a64-5be1485207d6)
![Screenshot (113)](https://github.com/user-attachments/assets/93c60da2-f6b3-45fe-8758-c719231c8ac3)
![Screenshot (112)](https://github.com/user-attachments/assets/d9993313-79d1-4f5b-b9fc-9aecd3f5306e)
