# 🔐 Comparative File Encryption Tool

### AES • DES • Fernet | GUI Dashboard 

---

## 📌 Overview

The **Comparative File Encryption Tool** is a complete cybersecurity-based project that allows users to securely encrypt and decrypt files using multiple encryption algorithms.

This project integrates:

* 🔐 **AES-256 Encryption (Advanced & Secure)**
* ⚠️ **DES Encryption (Legacy for comparison)**
* 🧪 **Fernet Encryption (Basic Implementation)**

All features are combined into a **centralized GUI dashboard**, making the system easy to use and highly efficient.

![Picture](https://github.com/Itsyashasvibhati/AES-DES-File-Encryption-Decryption./blob/43054b5d4aa586d1f3cebc27b5b8142b2ecfe33d/Screenshot%202026-03-26%20223731.png)
---


![Picture2](https://github.com/Itsyashasvibhati/AES-DES-File-Encryption-Decryption./blob/09b8b1f92c6ea30e4c9c3e0391c39ee439a6d04f/Screenshot%202026-03-26%20223826.png)


## 🚀 Features

### 🔒 Security Features

* AES-256 encryption with CBC mode
* Password-based key generation (PBKDF2)
* Secure salt and IV handling
* Multi-layer encryption system

### 🖥 GUI Features

* Dark mode interface 🌙
* Easy file selection 📂
* Multi-file encryption support
* Progress bar for operations ⏳
* Central dashboard for tool selection

### ⚙️ Functional Features

* Encrypt & decrypt any file type (txt, pdf, images, etc.)
* Batch (multi-file) processing
* Separate modules for AES, DES, and Basic encryption
* Modular and scalable design

---

![picture3](https://github.com/Itsyashasvibhati/AES-DES-File-Encryption-Decryption./blob/76a23af667a56e47cbd59c68f4f32903b76cb03e/Screenshot%202026-03-26%20223929.png)


![picture4](https://github.com/Itsyashasvibhati/AES-DES-File-Encryption-Decryption./blob/5583a1009796133fb75488041744aafca4b70c84/Screenshot%202026-03-26%20224023.png)

## 📂 Project Structure

```
File-Encryption-Tool
│
├── main_dashboard.py         # Main GUI Dashboard
├── aes_gui_tool.py           # AES Advanced Encryption Tool
├── des_gui_tool.py           # DES Encryption Tool (Comparison)
├── gui_encryption_tool.py    # Basic Fernet GUI Tool
├── encrypt.py                # Basic CLI Encryption
├── decrypt.py                # Basic CLI Decryption
├── generate_key.py           # Key generator
├── key.key                   # Generated key file
├── sample.txt                # Sample file for testing
├── secure-pdf.pdf            # Test file
└── README.md                 # Project documentation
```

---

## ⚙️ Technologies Used

* **Python 3.x**
* **Tkinter** (GUI Development)
* **Cryptography Library** (Fernet)
* **PyCryptodome** (AES & DES)
* **Hashlib** (Password hashing)

---

## 🔐 Encryption Algorithms Used

### 🔹 AES (Advanced Encryption Standard)

* Key Size: 256-bit
* Mode: CBC
* Security: Very High
* Used in modern systems

### 🔹 DES (Data Encryption Standard)

* Key Size: 56-bit
* Security: Weak (used for learning & comparison)

### 🔹 Fernet (Basic)

* Built on AES
* Easy implementation
* Suitable for beginners

---

## ▶️ How to Run the Project

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/file-encryption-tool.git
cd file-encryption-tool
```

### 2️⃣ Install Dependencies

```
pip install cryptography
pip install pycryptodome
```

### 3️⃣ Run Dashboard

```
python main_dashboard.py
```

---

## 🧑‍💻 How to Use

1. Open the dashboard
2. Select encryption method (AES / DES / Basic)
3. Select file(s)
4. Enter password
5. Click Encrypt or Decrypt

---

## 🔄 Workflow

```
User → Dashboard → Select Algorithm → Select File(s) → Enter Password
     → Encryption/Decryption → Output File
```

---
![image](https://github.com/Itsyashasvibhati/AES-DES-File-Encryption-Decryption./blob/9121c657bd8554dc6d18c812a92b06742a72134a/Screenshot%202026-03-26%20225233.png)

## 📊 Comparison (AES vs DES vs Fernet)

| Feature  | AES             | DES        | Fernet     |
| -------- | --------------- | ---------- | ---------- |
| Key Size | 128/192/256-bit | 56-bit     | 128-bit    |
| Security | Very Strong     | Weak       | Strong     |
| Speed    | Fast            | Slow       | Moderate   |
| Usage    | Modern          | Deprecated | Simplified |

---

## 🌍 Applications

* Secure file storage
* Safe data transmission
* Cloud security
* Personal data protection
* Cybersecurity education

---

## ✅ Advantages

* Strong data security using AES-256
* Multi-algorithm comparison
* User-friendly GUI
* Multi-file encryption support
* Scalable architecture

---

## ⚠️ Limitations

* DES is not secure (used only for learning)
* Password recovery not possible
* GUI limited to desktop environment

---

## 🔮 Future Enhancements

* Drag & drop file support
* Login authentication system 🔐
* Encryption history/logs 📊
* Cloud integration ☁️
* Convert to executable (.exe)
* Mobile application version 📱

---

## 🧠 Learning Outcomes

* Understanding of encryption algorithms
* Practical implementation of AES & DES
* GUI development using Tkinter
* Cybersecurity fundamentals

---

## 📌 Conclusion

This project demonstrates the practical implementation of modern encryption techniques using a user-friendly interface. It highlights the importance of secure data handling and provides a comparative study of encryption algorithms, making it both a functional tool and a learning platform.

---

## 🙌 Acknowledgment

This project was developed as part of a **Security Lab Project** to explore real-world applications of cryptography and cybersecurity.

---

## ⭐ Author

**Yashasvi Bhati**
B.Tech Computer Science Engineering
Security & Development Enthusiast 🚀

---

## 🌟 Show Your Support

If you like this project:

⭐ Star this repository
🍴 Fork it
📢 Share it

---

## 📬 Contact

For queries or collaboration:

* GitHub: https://github.com/Itsyashasvibhati
* LinkedIn: (www.linkedin.com/in/yashasvi-bhati-8444b82a1)

---

# 🔥 “Security is not a product, it's a process.”

---
