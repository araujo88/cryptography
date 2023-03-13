import os
from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    with open(file_path, 'wb') as f:
        f.write(encrypted)

def encrypt_directory(directory_path, key):
    for dirpath, _, filenames in os.walk(directory_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            encrypt_file(file_path, key)

def main():
    key = Fernet.generate_key()
    encrypt_directory('/path/to/directory', key)
    with open('key.txt', 'wb') as f:
        f.write(key)

if __name__ == '__main__':
    main()
