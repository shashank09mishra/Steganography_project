from PIL import Image
from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(password):
    # Generate a 32-byte key using SHA-256 hash of the password
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def encode_message(image_path, message, password, output_path):
    key = generate_key(password)
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())

    image = Image.open(image_path)
    encoded_image = image.copy()
    width, height = image.size

    # Convert the encrypted message to binary
    binary_message = ''.join(format(byte, '08b') for byte in encrypted_message) + "11111111"

    data_index = 0
    for x in range(width):
        for y in range(height):
            pixel = list(encoded_image.getpixel((x, y)))
            for i in range(3):
                if data_index < len(binary_message):
                    pixel[i] = pixel[i] & ~1 | int(binary_message[data_index])
                    data_index += 1
            encoded_image.putpixel((x, y), tuple(pixel))
            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    encoded_image.save(output_path)
    print("Message encoded successfully!")
