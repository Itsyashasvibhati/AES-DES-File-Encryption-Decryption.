from cryptography.fernet import Fernet

# Generate a secure key
key = Fernet.generate_key()

# Save key to file
with open("key.key", "wb") as key_file:
    key_file.write(key)

print("Key generated successfully!")
