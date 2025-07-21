# 🧠 Cybersecurity & Python Utilities

A curated collection of Python-based tools for cybersecurity, encryption, and system utilities. Built for educational purposes, ethical hacking practice, and hands-on learning.

---

## 🛡️ Security & Hacking Tools

### 🔐 Hash_Cracker.py
- Cracks hashes (like MD5, SHA-1, etc.) using a wordlist or brute-force with customizable character sets and lengths.
- Supports multithreading and progress tracking via `tqdm`.

### 🌐 Network_scaner.py
- Scans an entire network using ARP requests and lists connected devices with IP, MAC address, and hostname.
- Useful for LAN monitoring and auditing.

### 🚪 Port_Scanner.py / port_scanner.py
- Scans a target host for open TCP ports.
- Fetches service banners and displays results with color-coded formatting.
- Multithreaded for fast performance.

### 🌍 dns_enum.py
- Enumerates subdomains of a target domain using a wordlist.
- Helps in reconnaissance during web application testing.

### 🕵️‍♂️ info_stealer.py
- Extracts saved Chrome passwords (locally), clipboard data, and system info (like IP, MAC, hostname).
- Demonstrates the importance of device-level security and encryption.
- ⚠️ **Educational use only** – do not use unethically.

---

## 🧠 Cryptography

### 🏛️ caesar_cypher.py / caeser cypher.py
- Simple Caesar cipher encryption and decryption tool.
- Shifts letters by a fixed number for encoding messages.
- Great for learning the basics of classical encryption.

### 🔐 password strength
- Checks the strength of a password.
- May include checks for length, complexity, and use of common patterns.

---

## 📄 File & PDF Utilities

### 🔐 pdf_protection.py
- Creates a PDF file and encrypts it with a password.
- Uses `reportlab` and `PyPDF2`.

---

## 📱 Miscellaneous

### 📷 qr_code.py
- Generates QR codes from text or URLs.
- Useful for quick info sharing or testing QR functionality.

---

## ✅ Requirements

Install the dependencies using:

```bash
pip install -r requirements.txt

---

## Dependencies may include:

- scapy
- PyPDF2
- reportlab
- pycryptodome
- pikepdf
- pyperclip
- tqdm
- termcolor
- requests
- qrcode

---

##📚 License
This repository is for learning and ethical testing only. Do not use any tool here for unauthorized access or activity.

