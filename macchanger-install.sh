#!/usr/bin/env bash
# macchanger-install.sh
# Multi-arch installer for MacChanger AppImage (x86_64, aarch64/arm64, armhf/armv7l)
#
# What you must edit:
#   - Set BASE_URL to where YOU host the AppImages (GitHub Releases, Nutronix, etc.)
#   - Ensure your release files are named EXACTLY like:
#       MacChanger-x86_64.AppImage
#       MacChanger-aarch64.AppImage
#       MacChanger-armhf.AppImage
#
# Usage:
#   chmod +x macchanger-install.sh
#   ./macchanger-install.sh
#
# Uninstall:
#   ./macchanger-install.sh --uninstall

set -euo pipefail

APP_NAME="MacChanger"
INSTALL_DIR="/opt/macchanger"
BIN_PATH="${INSTALL_DIR}/MacChanger.AppImage"
DESKTOP_PATH="/usr/share/applications/macchanger.desktop"

# =========================
# EDIT THIS BASE URL
# Example (GitHub Releases):
# BASE_URL="https://github.com/<YOU>/<REPO>/releases/latest/download"
# Example (your own host):
# BASE_URL="https://downloads.nutronix.pw/macchanger"
# =========================
BASE_URL="https://YOUR-DOMAIN-OR-GITHUB-RELEASES-HERE"

need_root() {
  if [[ "${EUID:-$(id -u)}" -ne 0 ]]; then
    echo "This installer must run as root. Re-run with: sudo $0"
    exit 1
  fi
}

detect_arch() {
  local uarch
  uarch="$(uname -m)"

  case "$uarch" in
    x86_64|amd64)
      echo "x86_64"
      ;;
    aarch64|arm64)
      echo "aarch64"
      ;;
    armv7l|armv7|armhf)
      echo "armhf"
      ;;
    *)
      echo "Unsupported CPU architecture: ${uarch}"
      echo "Supported: x86_64, aarch64/arm64, armhf/armv7l"
      exit 1
      ;;
  esac
}

ensure_deps() {
  # curl or wget
  if command -v curl >/dev/null 2>&1; then
    return 0
  fi
  if command -v wget >/dev/null 2>&1; then
    return 0
  fi

  echo "Neither curl nor wget found. Installing curl..."
  if command -v apt >/dev/null 2>&1; then
    apt update
    apt install -y curl
  elif command -v dnf >/dev/null 2>&1; then
    dnf install -y curl
  elif command -v pacman >/dev/null 2>&1; then
    pacman -Sy --noconfirm curl
  else
    echo "No supported package manager found. Please install curl or wget."
    exit 1
  fi
}

download_file() {
  local url="$1"
  local out="$2"

  if command -v curl >/dev/null 2>&1; then
    curl -fL "$url" -o "$out"
  else
    wget -O "$out" "$url"
  fi
}

install_appimage() {
  local arch="$1"
  local filename="${APP_NAME}-${arch}.AppImage"
  local url="${BASE_URL}/${filename}"

  if [[ "$BASE_URL" == "https://YOUR-DOMAIN-OR-GITHUB-RELEASES-HERE" ]]; then
    echo "ERROR: You must edit BASE_URL inside this script first."
    echo "Set BASE_URL to the location where your AppImages are hosted."
    exit 1
  fi

  echo "Detected architecture: ${arch}"
  echo "Downloading: ${url}"

  mkdir -p "$INSTALL_DIR"

  local tmp="/tmp/${filename}"
  rm -f "$tmp"
  download_file "$url" "$tmp"

  chmod +x "$tmp"
  mv -f "$tmp" "$BIN_PATH"
  chmod +x "$BIN_PATH"

  echo "Installed AppImage to: ${BIN_PATH}"
}

install_desktop_entry() {
  # Icon uses a stock theme icon; you can replace with your own later.
  cat > "$DESKTOP_PATH" <<EOF
[Desktop Entry]
Type=Application
Name=MacChanger
Comment=Change MAC address (requires admin)
Exec=pkexec ${BIN_PATH}
Icon=network-wired
Terminal=false
Categories=System;Network;
StartupNotify=true
EOF

  chmod 644 "$DESKTOP_PATH"

  # Update desktop DB if available
  if command -v update-desktop-database >/dev/null 2>&1; then
    update-desktop-database /usr/share/applications >/dev/null 2>&1 || true
  fi

  echo "Installed desktop launcher: ${DESKTOP_PATH}"
  echo "Find it in your app menu: MacChanger"
}

ensure_pkexec() {
  if command -v pkexec >/dev/null 2>&1; then
    return 0
  fi

  echo "pkexec not found. Installing policykit..."
  if command -v apt >/dev/null 2>&1; then
    apt update
    apt install -y policykit-1
  elif command -v dnf >/dev/null 2>&1; then
    dnf install -y polkit
  elif command -v pacman >/dev/null 2>&1; then
    pacman -Sy --noconfirm polkit
  else
    echo "No supported package manager found. Please install PolicyKit (pkexec)."
    exit 1
  fi
}

uninstall_all() {
  echo "Uninstalling MacChanger..."
  rm -rf "$INSTALL_DIR"
  rm -f "$DESKTOP_PATH"

  if command -v update-desktop-database >/dev/null 2>&1; then
    update-desktop-database /usr/share/applications >/dev/null 2>&1 || true
  fi

  echo "Removed:"
  echo "  ${INSTALL_DIR}"
  echo "  ${DESKTOP_PATH}"
  echo "Done."
}

main() {
  need_root

  if [[ "${1:-}" == "--uninstall" ]]; then
    uninstall_all
    exit 0
  fi

  ensure_deps
  ensure_pkexec

  local arch
  arch="$(detect_arch)"

  install_appimage "$arch"
  install_desktop_entry

  echo ""
  echo "Install complete."
  echo "Launch from your application menu or run:"
  echo "  pkexec ${BIN_PATH}"
}

main "$@"
