from tkinter import *
from tkinter import filedialog, messagebox, ttk
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import os

# Padding function
def pad(data):
    while len(data) % 16 != 0:
        data += b' '
    return data

def unpad(data):
    return data.rstrip(b' ')

# Generate key from password
def get_key(password, salt):
    return PBKDF2(password, salt, dkLen=32)

def browse_file():
    file_path = filedialog.askopenfilename()
    entry_file.delete(0, END)
    entry_file.insert(0, file_path)

    if file_path:
        size = os.path.getsize(file_path) / 1024
        label_size.config(text=f"File Size: {size:.2f} KB")

def encrypt_file():
    file_path = entry_file.get()
    password = entry_password.get()

    if not file_path or not password:
        messagebox.showerror("Error", "Select file and enter password")
        return

    try:
        progress['value'] = 20
        root.update()

        with open(file_path, "rb") as f:
            data = f.read()

        progress['value'] = 40
        root.update()

        salt = get_random_bytes(16)
        key = get_key(password, salt)
        cipher = AES.new(key, AES.MODE_CBC)

        encrypted_data = cipher.encrypt(pad(data))

        progress['value'] = 70
        root.update()

        with open(file_path, "wb") as f:
            f.write(salt + cipher.iv + encrypted_data)

        progress['value'] = 100
        root.update()

        messagebox.showinfo("Success", "AES Encryption Successful 🔐")
        progress['value'] = 0

    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt_file():
    file_path = entry_file.get()
    password = entry_password.get()

    if not file_path or not password:
        messagebox.showerror("Error", "Select file and enter password")
        return

    try:
        progress['value'] = 20
        root.update()

        with open(file_path, "rb") as f:
            file_data = f.read()

        salt = file_data[:16]
        iv = file_data[16:32]
        encrypted_data = file_data[32:]

        progress['value'] = 50
        root.update()

        key = get_key(password, salt)
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)

        decrypted_data = unpad(cipher.decrypt(encrypted_data))

        progress['value'] = 80
        root.update()

        with open(file_path, "wb") as f:
            f.write(decrypted_data)

        progress['value'] = 100
        root.update()

        messagebox.showinfo("Success", "AES Decryption Successful 🔓")
        progress['value'] = 0

    except Exception:
        messagebox.showerror("Error", "Wrong Password or Corrupted File")

# GUI
root = Tk()
root.title("AES Encryption Tool (Advanced)")
root.geometry("550x350")
root.configure(bg="#121212")

Label(root, text="🔐 AES-256 File Encryption Tool",
      font=("Arial", 16, "bold"),
      fg="white", bg="#121212").pack(pady=10)

frame = Frame(root, bg="#121212")
frame.pack(pady=10)

entry_file = Entry(frame, width=40)
entry_file.grid(row=0, column=0, padx=10)

Button(frame, text="Browse", command=browse_file,
       bg="#333", fg="white").grid(row=0, column=1)

Label(root, text="Enter Password:",
      fg="white", bg="#121212").pack()

entry_password = Entry(root, show="*", width=30)
entry_password.pack(pady=5)

label_size = Label(root, text="File Size:",
                   fg="white", bg="#121212")
label_size.pack(pady=5)

progress = ttk.Progressbar(root, length=300)
progress.pack(pady=10)

Button(root, text="Encrypt (AES-256)",
       width=20, bg="green", fg="white",
       command=encrypt_file).pack(pady=5)

Button(root, text="Decrypt (AES-256)",
       width=20, bg="blue", fg="white",
       command=decrypt_file).pack(pady=5)

root.mainloop()