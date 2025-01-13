from PIL import Image
from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(password):
    # Generate a 32-byte key using SHA-256 hash of the password
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def decode_message(image_path, password):
    key = generate_key(password)
    fernet = Fernet(key)

    image = Image.open(image_path)
    width, height = image.size

    binary_message = ""
    for x in range(width):
        for y in range(height):
            pixel = list(image.getpixel((x, y)))
            for i in range(3):
                binary_message += str(pixel[i] & 1)

    # Convert binary message to bytes
    all_bytes = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    encrypted_message = bytearray()
    for byte in all_bytes:
        if byte == "11111111":  # End of message delimiter
            break
        encrypted_message.append(int(byte, 2))

    try:
        # Decrypt the message using the password
        decrypted_message = fernet.decrypt(bytes(encrypted_message)).decode()
        return decrypted_message
    except Exception as e:
        print("Error:", e)
        return None
