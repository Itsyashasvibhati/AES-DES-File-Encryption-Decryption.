from tkinter import *
from tkinter import messagebox
import os

# Functions to open tools
def open_aes():
    os.system("python aes_gui_tool.py")

def open_des():
    os.system("python Des_gui_tool.py")

def open_basic():
    os.system("python gui_encryption_tool.py")

def show_info():
    messagebox.showinfo("About", 
    "Advanced File Encryption Tool\n\nIncludes:\n- AES (Secure)\n- DES (Legacy)\n- Basic Encryption")

# GUI Setup
root = Tk()
root.title("🔐 Cyber Security Encryption Suite")
root.geometry("600x400")
root.configure(bg="#0f172a")  # dark navy

# Title
Label(root, text="🔐 Encryption Dashboard",
      font=("Arial", 20, "bold"),
      fg="white", bg="#0f172a").pack(pady=20)

Label(root, text="Select Encryption Method",
      font=("Arial", 12),
      fg="#94a3b8", bg="#0f172a").pack()

# Buttons Frame
frame = Frame(root, bg="#0f172a")
frame.pack(pady=30)

# AES Button
Button(frame, text="AES Encryption 🔐",
       width=25, height=2,
       bg="#22c55e", fg="white",
       font=("Arial", 10, "bold"),
       command=open_aes).grid(row=0, column=0, padx=10, pady=10)

# DES Button
Button(frame, text="DES Encryption ⚠️",
       width=25, height=2,
       bg="#f59e0b", fg="white",
       font=("Arial", 10, "bold"),
       command=open_des).grid(row=0, column=1, padx=10, pady=10)

# Basic Button
Button(frame, text="Basic Encryption 🧪",
       width=25, height=2,
       bg="#3b82f6", fg="white",
       font=("Arial", 10, "bold"),
       command=open_basic).grid(row=1, column=0, padx=10, pady=10)

# Exit Button
Button(frame, text="Exit ❌",
       width=25, height=2,
       bg="#ef4444", fg="white",
       font=("Arial", 10, "bold"),
       command=root.quit).grid(row=1, column=1, padx=10, pady=10)

# Footer
Button(root, text="About Project",
       bg="#1e293b", fg="white",
       command=show_info).pack(pady=10)

Label(root, text="Developed for Security Lab Project",
      fg="#64748b", bg="#0f172a").pack()

root.mainloop()