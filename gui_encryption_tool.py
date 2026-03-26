from tkinter import *
from tkinter import filedialog, messagebox, ttk
from cryptography.fernet import Fernet
import hashlib
import base64
import os

# Convert password to key
def generate_key_from_password(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

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

    key = generate_key_from_password(password)
    fernet = Fernet(key)

    try:
        progress['value'] = 20
        root.update()

        with open(file_path, "rb") as file:
            data = file.read()

        progress['value'] = 50
        root.update()

        encrypted = fernet.encrypt(data)

        with open(file_path, "wb") as file:
            file.write(encrypted)

        progress['value'] = 100
        root.update()

        messagebox.showinfo("Success", "File Encrypted Successfully 🔐")
        progress['value'] = 0

    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt_file():
    file_path = entry_file.get()
    password = entry_password.get()

    if not file_path or not password:
        messagebox.showerror("Error", "Select file and enter password")
        return

    key = generate_key_from_password(password)
    fernet = Fernet(key)

    try:
        progress['value'] = 20
        root.update()

        with open(file_path, "rb") as file:
            data = file.read()

        progress['value'] = 50
        root.update()

        decrypted = fernet.decrypt(data)

        with open(file_path, "wb") as file:
            file.write(decrypted)

        progress['value'] = 100
        root.update()

        messagebox.showinfo("Success", "File Decrypted Successfully 🔓")
        progress['value'] = 0

    except Exception as e:
        messagebox.showerror("Error", "Wrong Password or Corrupted File")

# GUI Setup
root = Tk()
root.title("Advanced File Encryption Tool")
root.geometry("550x350")
root.configure(bg="#1e1e1e")  # Dark mode

Label(root, text="🔐 File Encryption Tool",
      font=("Arial", 18, "bold"),
      fg="white", bg="#1e1e1e").pack(pady=10)

frame = Frame(root, bg="#1e1e1e")
frame.pack(pady=10)

entry_file = Entry(frame, width=40)
entry_file.grid(row=0, column=0, padx=10)

Button(frame, text="Browse", command=browse_file,
       bg="#333", fg="white").grid(row=0, column=1)

Label(root, text="Enter Password:",
      fg="white", bg="#1e1e1e").pack()

entry_password = Entry(root, show="*", width=30)
entry_password.pack(pady=5)

label_size = Label(root, text="File Size: ",
                   fg="white", bg="#1e1e1e")
label_size.pack(pady=5)

progress = ttk.Progressbar(root, length=300)
progress.pack(pady=10)

Button(root, text="Encrypt File",
       width=20, bg="green", fg="white",
       command=encrypt_file).pack(pady=5)

Button(root, text="Decrypt File",
       width=20, bg="blue", fg="white",
       command=decrypt_file).pack(pady=5)

root.mainloop()