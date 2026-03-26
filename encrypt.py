from cryptography.fernet import Fernet

# Load the encryption key
with open("key.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Ask user for file name
file_name = input("Enter the file name to encrypt: ")

# Read file data
with open(file_name, "rb") as file:
    original = file.read()

# Encrypt the data
encrypted = fernet.encrypt(original)

# Write encrypted data back
with open(file_name, "wb") as encrypted_file:
    encrypted_file.write(encrypted)

print("✅ File encrypted successfully!")