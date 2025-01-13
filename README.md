# Steganography_project
This is my project of cybersecurity in sem 5
This Steganography Tool allows users to securely encode and decode messages into PNG images using a password. The tool uses Fernet encryption for securing messages and LSB (Least Significant Bit) encoding for hiding data in images.
this is the format of file 
![image](https://github.com/user-attachments/assets/3edc7d18-6c7c-4059-aded-9493f7066e2a)

Features

Encode Message

Encrypts the message with a user-provided password.

Hides the encrypted message in a PNG image.

Saves the encoded image for future use.

Decode Message

Extracts the hidden message from the encoded image.

Decrypts the message using the same password.

Prerequisites

Python 3.7+

Required Python Libraries:

Pillow

cryptography
How to Run

Encoding a Message

Run the main GUI script:

python main.py

Click "Encode Message".

Browse and select a PNG image file.

Enter the message to hide.

Provide a password for encryption.

Save the encoded image.

Decoding a Message

Run the main GUI script:

python main.py

Click "Decode Message".

Browse and select the encoded PNG image file.

Enter the password used during encoding.

If successful, the hidden message will be displayed.

Code Explanation

Key Functions

1. Encoding Message (encode.py):

generate_key(password):

Converts the password into a secure 32-byte key using SHA-256.

encode_message(image_path, message, password, output_path):

Encrypts the message using the generated key.

Hides the encrypted message in the image's LSBs.

2. Decoding Message (decode.py):

generate_key(password):

Generates the same key used during encoding.

decode_message(image_path, password):

Extracts binary data from the image.

Converts the binary data back to bytes and decrypts it.

Example Usage

Encoding Example
from encode import encode_message

encode_message(
    image_path="input_image.png",
    message="Hello, World!",
    password="securepassword",
    output_path="encoded_image.png"
)
Decoding Example
from decode import decode_message

message = decode_message(
    image_path="encoded_image.png",
    password="securepassword"
)
print("Decoded Message:", message)
