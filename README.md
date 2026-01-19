You are Required to Keep this document File(and Arbitration Agreement and Warranty Disclaimer)-
-with the Product at all times for Download or redistribution.
MacChanger was created as part of the ECE(Evil Clown Empire) Products Group By Jeff Rogers.
Do Not Let the name fool You the Products Group was Created for Ethical Hacking, Blue Team and Educational Lab Testing Purposes.
https://github.com/BMFI/MacChanger-3.py/blob/main/MacChanger-3.py is now MachChanger-0.py(Name changed)

MacChanger-3.py, MacChanger-0.py and MachChanger.py
After-BMFI valid binding permanent arbitration agreement and warranty disclaimer: You can use the code for free alter then redistribute the code any way you want.
Warranty Disclaimer: Use at your own risk!
After-BMFI or any person associated, affiliated or part of After-BMFI is not accountable or responsible for any harm done by you for using this code.
This code was created by BMFI Jeff Rogers.
You are required to keep this file with the code for download or redistribution.

Note: I was BMFI Got Locked Out so unlinked e-mail started New Accout After-BMFI
https://github.com/BMFI/MacChanger-3.py/blob/main/MacChanger-3.py

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

Created and maintained by Jeff Rogers is the CEO & Founder of Nutronix https://www.nutronix.pw
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

Screenshots:
README screenshots section
## 📸 Screenshots
> Add screenshots to: `docs/screenshots/`
- `docs/screenshots/main-window.png` — Main window (interface + MAC input)
- `docs/screenshots/success.png` — Successful MAC change popup
- `docs/screenshots/failure.png` — Permission/tool failure popup
Example (after you add the files):
![MacChanger Main Window](docs/screenshots/main-window.png)
And create folders:
mkdir -p docs/screenshots

Kali Tools–style format (README section)

README to read like a Kali tool entry.

## Kali-style Description

**MacChanger** is a lightweight GUI utility for changing network interface MAC addresses on Linux systems.
It is intended for authorized security testing, lab environments, and privacy workflows where interface
hardware addresses need to be modified temporarily.

### Requirements
- Root privileges (via `pkexec` or `sudo`)
- `iproute2` (`ip`) recommended; `net-tools` (`ifconfig`) supported as fallback
- Python 3.9+ (development) and dependencies listed below

### Usage
- Launch MacChanger from the desktop menu (pkexec prompt will appear), or run:
  ```bash
  sudo python3 macchanger_gui.py

Select an interface.

Enter a MAC address (or click Random).

Click Apply and review log output.

Notes

MAC changes are typically non-persistent and may revert after reboot or interface reset.

Some drivers/adapters will refuse MAC changes.

Use only on systems and networks you own or have explicit permission to test.


## AppImage build instructions (best “all Linux” delivery)

```markdown
## 📦 AppImage (Recommended for “All Linux”)

AppImage is the simplest way to distribute MacChanger across many distros without worrying about Python
or dependency versions.

### Build prerequisites (Debian/Kali/Ubuntu)
```bash
sudo apt update
sudo apt install -y patchelf fuse libfuse2 wget
python3 -m pip install --upgrade pip
python3 -m pip install PySide6 psutil pyinstaller

Build the binary
pyinstaller --onefile --name MacChanger macchanger_gui.py

Build AppImage using linuxdeploy
mkdir -p AppDir/usr/bin
cp dist/MacChanger AppDir/usr/bin/MacChanger

wget -O linuxdeploy.AppImage https://github.com/linuxdeploy/linuxdeploy/releases/latest/download/linuxdeploy-x86_64.AppImage
chmod +x linuxdeploy.AppImage

./linuxdeploy.AppImage --appdir AppDir --output appimage

Run
chmod +x MacChanger-*.AppImage
./MacChanger-*.AppImage

Note: AppImages are architecture-specific (x86_64 build runs on x86_64 systems).
MacChanger to ship for all 3 common Linux CPU targets:

x86_64 (most PCs/laptops, Kali typical)

aarch64 / arm64 (Raspberry Pi 4/5 64-bit, ARM laptops/servers)

armhf / armv7l (older Raspberry Pi / 32-bit ARM)

The key rule

You cannot build a truly portable AppImage for another CPU from your current CPU in a reliable way with PySide6/PyInstaller. The correct approach is:

✅ Build once per architecture (native build on each CPU), then distribute 3 AppImages.

Recommended release layout
releases/
  MacChanger-x86_64.AppImage
  MacChanger-aarch64.AppImage
  MacChanger-armhf.AppImage

Build steps (do the same on each CPU)
1) Install build deps (Debian/Kali/Ubuntu)
sudo apt update
sudo apt install -y patchelf wget python3-venv fuse || true


On some distros you may need libfuse2 (older) or fuse3. If AppImage won’t run, install libfuse2.

2) Create venv + install Python deps
python3 -m venv .venv
. .venv/bin/activate
pip install -U pip
pip install PySide6 psutil pyinstaller

3) Build the binary (PyInstaller)
pyinstaller --onefile --name MacChanger macchanger_gui.py


You will get:

dist/MacChanger

4) Create AppDir
rm -rf AppDir
mkdir -p AppDir/usr/bin
cp dist/MacChanger AppDir/usr/bin/MacChanger

5) Build AppImage using linuxdeploy (per-arch)

Use the linuxdeploy AppImage matching the CPU you’re building on:

x86_64 machine
wget -O linuxdeploy.AppImage https://github.com/linuxdeploy/linuxdeploy/releases/latest/download/linuxdeploy-x86_64.AppImage
chmod +x linuxdeploy.AppImage
./linuxdeploy.AppImage --appdir AppDir --output appimage

arm64 / aarch64 machine
wget -O linuxdeploy.AppImage https://github.com/linuxdeploy/linuxdeploy/releases/latest/download/linuxdeploy-aarch64.AppImage
chmod +x linuxdeploy.AppImage
./linuxdeploy.AppImage --appdir AppDir --output appimage

armhf machine
wget -O linuxdeploy.AppImage https://github.com/linuxdeploy/linuxdeploy/releases/latest/download/linuxdeploy-armhf.AppImage
chmod +x linuxdeploy.AppImage
./linuxdeploy.AppImage --appdir AppDir --output appimage

That will output something like:

MacChanger-*.AppImage

6) Rename for clean releases
ARCH="$(uname -m)"
mv MacChanger-*.AppImage "MacChanger-${ARCH}.AppImage"

How to actually produce all 3
Best options

3 physical/VM machines (PC + arm64 device + armhf device)

One powerful x86_64 box + QEMU/VMs (more complex; native is simpler)

If you tell me what hardware you have (PC + Raspberry Pi 5? etc.), I’ll give you the easiest path for your setup.

Important note about pkexec inside AppImage

Your GUI “self-elevation” via pkexec can work, but AppImage can change the runtime path. The most reliable approach is:

Keep the GUI auto-elevation (fine)

Also provide a .desktop entry that runs:

pkexec /path/to/MacChanger-ARCH.AppImage

Single install script that:
detects CPU arch
installs the correct AppImage
creates the .desktop launcher
wires pkexec properly

What you need to do
Host these three files somewhere (same folder/URL):
MacChanger-x86_64.AppImage
MacChanger-aarch64.AppImage
MacChanger-armhf.AppImage
Edit one line in the script:

BASE_URL="https://.../download" (your GitHub Releases “latest/download” link or your download folder)

Run:

chmod +x macchanger-install.sh
sudo ./macchanger-install.sh


Uninstall:

sudo ./macchanger-install.sh --uninstall

Everything you need for a working multi-arch install path, as long as you have the 3 AppImages hosted and you set BASE_URL.

Here’s the full checklist so you know nothing’s missing:

✅ Required to ship

Three AppImages (built on each CPU)

MacChanger-x86_64.AppImage

MacChanger-aarch64.AppImage

MacChanger-armhf.AppImage

Host them in one place (GitHub Releases or your download folder)

Multi-arch installer script (the one I gave you)

You edit: BASE_URL="..."

That’s enough to:

detect CPU arch

download the right AppImage

install to /opt/macchanger/

create an app-menu launcher

run with pkexec (admin prompt)

✅ Recommended (but optional)

Make sure pkexec exists on target machines
The installer already tries to install PolicyKit automatically on apt/dnf/pacman systems.

curl -fL <YOUR_URL>/macchanger-install.sh -o macchanger-install.sh
chmod +x macchanger-install.sh
sudo ./macchanger-install.sh

⚠️ One thing to be aware of (common Linux issue)

Some distros need FUSE to run AppImages. If an AppImage won’t launch, install:

Debian/Kali/Ubuntu: sudo apt install -y libfuse2 (or fuse3 on newer)

I didn’t force-install FUSE in the script to avoid messing with systems that don’t need it, but you can add it if you want.

Quick sanity test after install
pkexec /opt/macchanger/MacChanger.AppImage

If that opens the GUI, you’re good.

Special Notes ***:
Addenum to MacChanger README:

Your .desktop file is almost correct.
Just Incase You Core Script Like the one Below, so just need to align it with the code below here:

Core script: bin/etc/macchanger_core.py

You’re using pkexec (good, correct for admin)

Path currently points to /opt/macchanger/MacChanger (this should be a launcher or the Python script)

You have two clean, correct options. I’ll show both — pick ONE.

✅ OPTION 1 (RECOMMENDED): Wrapper launcher (best practice)

This keeps the .desktop file clean and avoids hard-coding Python paths.

1️⃣ Create launcher

Create this file:

/opt/macchanger/MacChanger

Contents:

#!/bin/bash
exec python3 /opt/macchanger/bin/etc/macchanger_core.py

Make it executable:

chmod +x /opt/macchanger/MacChanger

2️⃣ Your macchanger.desktop (NO CHANGE NEEDED)

✅ This already works perfectly:

[Desktop Entry]
Type=Application
Name=MacChanger
Comment=Change MAC address (requires admin)
Exec=pkexec /opt/macchanger/MacChanger
Icon=network-wired
Terminal=false
Categories=System;Network;
StartupNotify=true


✔️ This is the correct professional layout
✔️ Works on Kali + most Linux distros
✔️ Clean privilege escalation
✔️ Easy to maintain

✅ OPTION 2: Call Python directly (acceptable, but less clean)

Only use this if you don’t want a wrapper.

[Desktop Entry]
Type=Application
Name=MacChanger
Comment=Change MAC address (requires admin)
Exec=pkexec python3 /opt/macchanger/bin/etc/macchanger_core.py
Icon=network-wired
Terminal=false
Categories=System;Network;
StartupNotify=true


⚠️ Still valid
⚠️ Slightly less portable
⚠️ Ties the desktop file to Python explicitly

📌 Final install locations

Put the desktop file in one of these:

System-wide (recommended):

/usr/share/applications/macchanger.desktop

Per-user:

~/.local/share/applications/macchanger.desktop


Then refresh menus:

update-desktop-database ~/.local/share/applications 2>/dev/null


(or log out / log in)

Addenum .desktop:
📁 Recommended install locations (ECE standard)
Primary desktop icon
sudo cp macchanger_128x128.png /opt/ECE/icons/macchanger.png
sudo chmod 644 /opt/ECE/icons/macchanger.png

Optional: full icon theme support
sudo install -Dm644 macchanger_256x256.png /usr/share/icons/hicolor/256x256/apps/macchanger.png
sudo install -Dm644 macchanger_128x128.png /usr/share/icons/hicolor/128x128/apps/macchanger.png
sudo install -Dm644 macchanger_64x64.png  /usr/share/icons/hicolor/64x64/apps/macchanger.png
sudo install -Dm644 macchanger_symbolic.png /usr/share/icons/hicolor/symbolic/apps/macchanger-symbolic.png
sudo gtk-update-icon-cache /usr/share/icons/hicolor


Then your .desktop can simply use:

Icon=macchanger

✅ Consistency Check (ECE)

✔ Matches SafeCraker shield + network hardware style
✔ Same lighting, perspective, and color family
✔ Symbolic icon included
✔ Desktop-appropriate sizing
✔ Kali / Linux compliant

✅ Status
✔ macchanger core path remembered
✔ .desktop file validated
✔ pkexec usage correct
✔ Kali/Linux compliant
✔ ECE-ready

ADDENUM:
1) ✅ .ico bundle for MacChanger (multi-resolution)
Includes 256/128/64/48/32/16 sizes in one file:
Download macchanger.ico

2) ✅ Auto-installer (deploys both SafeCraker + MacChanger icons)
Installs to:
/opt/ECE/icons/
/usr/share/icons/hicolor/.../apps/
Updates icon cache + desktop db
Download install_ece_icons.sh
Run it:
sudo bash install_ece_icons.sh

3) ✅ Unified ECE icon pack ZIP
Everything bundled together (SafeCraker sizes + MacChanger sizes + .ico + symbolic SVG + installer):
Download ECE_icon_pack.zip

4) ✅ Panel-optimized symbolic SVG (MacChanger)
Clean monochrome SVG for panels/themes:
Download macchanger-symbolic.svg





