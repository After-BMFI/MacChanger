Note: I was BMFI Got Locked Out so unlinked e-mail started New Accout After-BMFI
https://github.com/BMFI/MacChanger-3.py/blob/main/MacChanger-3.py

After-BMFI Licenes Agreement:
After-BMFI valid binding permanent arbitration agreement and warranty disclaimer:
You can use the code for free alter then redistribute the code any way you want.
Warranty Disclaimer: Use at your own risk!
BMFI or any person associated, affiliated or part of BMFI is not accountable or responsible for any harm done by you for using this code.
This code was created by BMFI Jeff Rogers.
You are required to keep this file with the code for download or redistribution.


# MacChanger
New Improved 2026
# MacChanger

**MacChanger** is a modern, Linux-first MAC address changer with a graphical interface built using **PySide6 (Qt)**.  
It is designed for **Kali Linux** and other modern Linux distributions, with proper privilege handling via **pkexec**.

> ⚠️ Root/admin privileges are required to change MAC addresses on Linux.

---

## ✨ Features

- ✅ Graphical desktop application (Qt / PySide6)
- ✅ Python **3.9–3.12** compatible
- ✅ Kali Linux friendly
- ✅ Uses modern `ip` tool (fallback to `ifconfig`)
- ✅ Automatic admin elevation via **pkexec**
- ✅ Lists available network interfaces
- ✅ Displays current MAC address
- ✅ Validates MAC address input
- ✅ Generates random locally administered MAC addresses
- ✅ Session-based restore (restore MAC from app launch)
- ✅ Detailed command output log
- ✅ Standalone Linux binary (no Python required on target)

---

## 🖥️ Supported Platforms

| OS | Status |
|----|-------|
| Kali Linux | ✅ Fully supported |
| Debian / Ubuntu | ✅ Supported |
| Linux Mint | ✅ Supported |
| Arch Linux | ✅ Supported |
| Fedora | ✅ Supported |
| Windows | ⚠️ Experimental / driver-dependent |

> Linux is the primary supported platform.

---

## 🐍 Python Requirements (Development Only)

- **Python 3.9 – 3.12**
- Not compatible with Python < 3.9

Once packaged as a binary, Python is **not required** on the target machine.

---

## 📦 Dependencies (Development)

```bash
pip install PySide6 psutil pyinstaller

