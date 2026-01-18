#Create uninstall_linux.sh
#!/usr/bin/env bash
set -e

sudo rm -rf /opt/macchanger
rm -f ~/.local/share/applications/macchanger.desktop

command -v update-desktop-database >/dev/null 2>&1 && update-desktop-database ~/.local/share/applications || true

echo "MacChanger removed."
