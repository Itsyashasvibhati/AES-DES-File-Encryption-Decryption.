from cryptography.fernet import Fernet

# Load key
with open("key.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

print("🔓 File Decryption Tool")

file_name = input("Enter the file name to decrypt: ")

with open(file_name, "rb") as file:
    encrypted_data = file.read()

decrypted_data = fernet.decrypt(encrypted_data)

with open(file_name, "wb") as file:
    file.write(decrypted_data)

print("✅ File decrypted successfully!")