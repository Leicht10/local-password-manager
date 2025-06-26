# 🔐 Local Password Manager (Python)

This is a fully offline, menu-driven password manager built in Python.  
It encrypts passwords using randomized substitution and secures access with a master password.

---

## 💡 Features

- 🔁 Generates 10 unique encryption keys (stored in `keys.txt`)
- 🔒 Stores encrypted passwords in `passwords.txt`
- 🔐 Master password required to decrypt passwords
- 🧠 Simple substitution cipher logic
- 🖥️ Command-line interface (menu system)
- 🧾 All data stored locally, no internet or database needed

---

## 🛠️ How It Works

- You define a master password
- When storing a password:
  - A random encryption key (0–9) is chosen
  - The password is encrypted using character substitution
  - Encrypted password + key index is stored
- When retrieving:
  - You enter the master password
  - The correct key is used to decrypt and show the password

---

## 🔧 Files Created

- `keys.txt` — 10 randomly shuffled keys used for encryption
- `passwords.txt` — stores website and encrypted password pairs

Example:

website: gmail.com
password: jD#9&z7Ax5


---

## 📦 Setup

1. Clone this repository
2. Run the script:

```bash
python password_manager.py
```

## 🧠 Why I Built This

I wanted to build a local, offline password manager from scratch. I came up with the idea of using random character substitution, and used AI to help correct and improve the code I wrote. This project helped me practice:

1. Encryption logic
2. File I/O in Python
3. Data security concepts
4. Command-line interaction

## 🛡️ Security Notes

1. Do not delete keys.txt — it is required for decryption
2. All data is stored locally
3. The master password is hardcoded — for real use, replace with secure input method
