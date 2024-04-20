import os
import zipfile
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from getpass import getpass

def encrypt_folder(input_folder, output_filename):
    # Get a password from the user
    password = getpass("Enter encryption password: ")

    # Derive a key from the password using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=algorithms.SHA256(),  # Use a hash function, not an encryption algorithm
        length=32,
        salt=os.urandom(16),
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    # Create a Zip file and add all files from the folder
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_BZIP2) as zipf:
        for root, dirs, files in os.walk(input_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, input_folder)
                zipf.write(file_path, arcname=arcname)

    # Encrypt the Zip file
    with open(output_filename, 'rb') as file:
        data = file.read()
        cipher = Cipher(algorithms.SM4(key), modes.CFB(os.urandom(16)), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(data) + encryptor.finalize()

    with open(output_filename, 'wb') as file:
        file.write(encrypted_data)

    print(f'Encryption successful. Encrypted file: {output_filename}')

# Example usage
input_folder = 'target_folder'
output_filename = 'encrypted_target_folder.zip'

encrypt_folder(input_folder, output_filename)
