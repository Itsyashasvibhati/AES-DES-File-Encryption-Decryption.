from tkinter import *
from tkinter import filedialog, messagebox
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import hashlib
import os

def get_des_key(password):
    # DES needs 8 bytes key
    return hashlib.md5(password.encode()).digest()[:8]

def browse_file():
    file_path = filedialog.askopenfilename()
    entry_file.delete(0, END)
    entry_file.insert(0, file_path)

def encrypt_file():
    file_path = entry_file.get()
    password = entry_password.get()

    if not file_path or not password:
        messagebox.showerror("Error", "Select file and enter password")
        return

    try:
        key = get_des_key(password)
        cipher = DES.new(key, DES.MODE_ECB)

        with open(file_path, "rb") as f:
            data = f.read()

        encrypted = cipher.encrypt(pad(data, 8))

        with open(file_path, "wb") as f:
            f.write(encrypted)

        messagebox.showinfo("Success", "DES Encryption Done")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt_file():
    file_path = entry_file.get()
    password = entry_password.get()

    try:
        key = get_des_key(password)
        cipher = DES.new(key, DES.MODE_ECB)

        with open(file_path, "rb") as f:
            data = f.read()

        decrypted = unpad(cipher.decrypt(data), 8)

        with open(file_path, "wb") as f:
            f.write(decrypted)

        messagebox.showinfo("Success", "DES Decryption Done")

    except:
        messagebox.showerror("Error", "Wrong Password or File")

# GUI
root = Tk()
root.title("DES Encryption Tool")
root.geometry("500x250")

Label(root, text="DES Encryption Tool", font=("Arial", 16)).pack(pady=10)

entry_file = Entry(root, width=40)
entry_file.pack(pady=5)

Button(root, text="Browse", command=browse_file).pack()

Label(root, text="Password").pack()
entry_password = Entry(root, show="*")
entry_password.pack(pady=5)

Button(root, text="Encrypt (DES)", command=encrypt_file).pack(pady=5)
Button(root, text="Decrypt (DES)", command=decrypt_file).pack(pady=5)

root.mainloop()