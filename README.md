Note: I was BMFI Got Locked Out so unlinked e-mail started New Accout After-BMFI
https://github.com/BMFI/MacChanger-3.py/blob/main/MacChanger-3.py

After-BMFI License Agreement:
This project is provided as-is for educational, testing, and authorized security research purposes.
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

Make executable:
chmod +x install_linux.sh


Run install:
./install_linux.sh

System tools (usually already installed on Kali):
iproute2 (ip)
policykit-1 (pkexec)

▶️ Running from Source (Linux)
sudo python3 macchanger_gui.py
The app will automatically relaunch itself using pkexec if not already running as root.

🛠️ Building a Standalone Linux Binary
Run this on Linux only:
./build_linux.sh

Output:
dist/MacChanger

📥 Installing the Application (System Integration)
./install_linux.sh
This will:
Install the binary to /opt/macchanger/MacChanger
Add a desktop launcher to your app menu
Enable GUI admin prompts via pkexec
Launch it from your application menu as MacChanger.

🗑️ Uninstalling
./uninstall_linux.sh

🔐 Privileges & Security Notes
Changing MAC addresses requires root access
This app uses pkexec (PolicyKit) for safe GUI elevation
No background services are installed
No network data is transmitted
Use only on networks and systems you own or have permission to test.

📁 Project Structure
MacChanger/
├── macchanger_core.py     # Core MAC-changing logic
├── macchanger_gui.py      # PySide6 GUI + pkexec elevation
├── pyproject.toml         # Python version & dependency lock
├── macchanger.desktop     # Desktop launcher
├── build_linux.sh         # Binary build script
├── install_linux.sh       # Install script
├── uninstall_linux.sh     # Uninstall script
└── README.md

🚧 Known Limitations

Linux MAC changes are temporary (reset on reboot unless managed externally)

Some interfaces (e.g., virtual, monitor mode, or driver-locked adapters) may refuse MAC changes

Windows support is driver-dependent and not guaranteed

📜 License
After-BMFI
This project is provided as-is for educational, testing, and authorized security research purposes.


👤 Author

Created and maintained by Jeff Rogers is the CEO and Founder of Nutronix https://www.nutronix.pw
Nutronix.pw also the Creator of BMFI on GitHub
⭐ Final Notes
MacChanger is designed to behave like a professional Kali tool:
Clean GUI
Explicit privilege handling
Minimal dependencies
No hacks or unsafe shortcuts
If you plan to distribute publicly, consider packaging as an AppImage for maximum Linux compatibility.

pyproject.toml: Notes.
pyproject.toml is treated as a control file by Python tools
This behavior comes from Python Enhancement Proposals (PEPs):
PEP 518
PEP 621
These PEPs say (simplified):
If a file named pyproject.toml exists,
Python tooling MUST load and interpret it.
So tools like:
pip
setuptools
build
poetry
hatch
will always open pyproject.toml, even if:
it only has comments
it has “notes”
it has no [project] section
it looks inactive to a human
👉 The filename is the trigger, not the content.







