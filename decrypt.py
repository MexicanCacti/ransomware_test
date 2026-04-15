import sys
from pathlib import Path
from cryptography.fernet import Fernet

# Note: Install cryptography library using pip if you haven't already:
# pip install cryptography

def decrypt_directory(root, key):
    for item in root.rglob("*"):
        if item.is_file():
            try:
                data = item.read_bytes()
                decrypted = key.decrypt(data)
                item.write_bytes(decrypted)
                print(f"Decrypted: {item}")
            except Exception as e:
                print(f"Error on {item}: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python decrypt.py <BASE64_KEY>")
        sys.exit(1)

    encodedKey = sys.argv[1].encode()
    key = Fernet(encodedKey)

    root = Path.cwd()
    for subdir in root.iterdir():
        if subdir.is_dir():
            decrypt_directory(subdir, key)

if __name__ == "__main__":
    main()