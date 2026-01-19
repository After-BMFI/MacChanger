
CHANGELOG.md
# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog, and this project follows Semantic Versioning.

## [1.0.0] - 2026-01-18
### Added
- PySide6 (Qt) desktop GUI for changing MAC addresses.
- Linux-first implementation using `ip` with fallback to `ifconfig`.
- Interface picker with current MAC display.
- MAC validation and normalization.
- Random locally administered MAC generator.
- Session-based restore (restore MAC captured at app launch).
- Detailed command log output in the GUI.
- Optional system integration scripts (build/install/uninstall).
- Desktop launcher support with pkexec elevation.

- 📁 Recommended install locations (ECE standard)
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
