#macchanger_gui.py (self-elevates on Linux + Qt GUI)
#!/usr/bin/env python3
import os
import sys
import subprocess

def ensure_root_linux():
    if sys.platform.startswith("linux"):
        try:
            is_root = (os.geteuid() == 0)
        except AttributeError:
            is_root = False

        if not is_root:
            # Relaunch via pkexec
            env = os.environ.copy()
            display = env.get("DISPLAY", "")
            xauth = env.get("XAUTHORITY", os.path.expanduser("~/.Xauthority"))

            cmd = [
                "pkexec",
                "env",
                f"DISPLAY={display}",
                f"XAUTHORITY={xauth}",
                os.path.abspath(sys.argv[0]),
            ]
            # pass through args
            cmd.extend(sys.argv[1:])

            try:
                subprocess.Popen(cmd)
            except FileNotFoundError:
                print("pkexec not found. Install policykit or run with sudo.")
            sys.exit(0)

ensure_root_linux()

import psutil
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QComboBox, QLineEdit, QPushButton,
    QPlainTextEdit, QVBoxLayout, QHBoxLayout, QMessageBox, QGroupBox
)

from macchanger_core import change_mac, normalize_mac, is_valid_mac, random_mac

APP_NAME = "MacChanger"

def list_interfaces() -> list[str]:
    names = list(psutil.net_if_addrs().keys())
    names.sort(key=str.lower)
    # skip loopback if present
    names = [n for n in names if n != "lo"]
    return names

def get_current_mac(interface: str) -> str:
    addrs = psutil.net_if_addrs().get(interface, [])
    for a in addrs:
        addr = getattr(a, "address", "") or ""
        addr2 = addr.lower().replace("-", ":")
        if is_valid_mac(addr2):
            return addr2
    return ""

class MacChangerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_NAME)
        self.setMinimumWidth(760)

        self.original_macs: dict[str, str] = {}

        title = QLabel(f"<h2>{APP_NAME}</h2>")
        subtitle = QLabel("Linux requires admin/root. This app will prompt using pkexec.")
        subtitle.setWordWrap(True)

        iface_box = QGroupBox("Adapter")
        iface_layout = QHBoxLayout()
        self.iface_combo = QComboBox()
        self.refresh_btn = QPushButton("Refresh")
        iface_layout.addWidget(QLabel("Interface:"))
        iface_layout.addWidget(self.iface_combo, 1)
        iface_layout.addWidget(self.refresh_btn)
        iface_box.setLayout(iface_layout)

        cur_box = QGroupBox("Current MAC")
        cur_layout = QHBoxLayout()
        self.current_mac_label = QLabel("(select an interface)")
        self.current_mac_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        cur_layout.addWidget(self.current_mac_label, 1)
        cur_box.setLayout(cur_layout)

        mac_box = QGroupBox("New MAC")
        mac_layout = QHBoxLayout()
        self.mac_input = QLineEdit()
        self.mac_input.setPlaceholderText("00:11:22:33:44:55")
        self.valid_label = QLabel("✗")
        self.valid_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        mac_layout.addWidget(QLabel("MAC:"))
        mac_layout.addWidget(self.mac_input, 1)
        mac_layout.addWidget(self.valid_label)
        mac_box.setLayout(mac_layout)

        btns = QHBoxLayout()
        self.random_btn = QPushButton("Random")
        self.restore_btn = QPushButton("Restore (session)")
        self.apply_btn = QPushButton("Apply")
        self.apply_btn.setDefault(True)
        self.clear_log_btn = QPushButton("Clear Log")

        btns.addWidget(self.random_btn)
        btns.addWidget(self.restore_btn)
        btns.addStretch(1)
        btns.addWidget(self.clear_log_btn)
        btns.addWidget(self.apply_btn)

        self.log = QPlainTextEdit()
        self.log.setReadOnly(True)
        self.log.setPlaceholderText("Command output will appear here...")

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(iface_box)
        layout.addWidget(cur_box)
        layout.addWidget(mac_box)
        layout.addLayout(btns)
        layout.addWidget(QLabel("Log"))
        layout.addWidget(self.log, 1)
        self.setLayout(layout)

        self.refresh_btn.clicked.connect(self.refresh_interfaces)
        self.iface_combo.currentTextChanged.connect(self.on_iface_changed)
        self.mac_input.textChanged.connect(self.on_mac_changed)
        self.random_btn.clicked.connect(self.on_random)
        self.restore_btn.clicked.connect(self.on_restore)
        self.apply_btn.clicked.connect(self.on_apply)
        self.clear_log_btn.clicked.connect(lambda: self.log.setPlainText(""))

        self.refresh_interfaces()

    def append_log(self, text: str):
        text = (text or "").strip()
        if not text:
            return
        existing = self.log.toPlainText().rstrip()
        self.log.setPlainText((existing + "\n\n" + text).strip() if existing else text)
        self.log.verticalScrollBar().setValue(self.log.verticalScrollBar().maximum())

    def refresh_interfaces(self):
        current = self.iface_combo.currentText().strip()
        self.iface_combo.clear()
        for name in list_interfaces():
            self.iface_combo.addItem(name)
        if current:
            idx = self.iface_combo.findText(current)
            if idx >= 0:
                self.iface_combo.setCurrentIndex(idx)
        self.on_iface_changed(self.iface_combo.currentText())

    def on_iface_changed(self, iface: str):
        iface = (iface or "").strip()
        mac = get_current_mac(iface) if iface else ""
        if iface and iface not in self.original_macs:
            self.original_macs[iface] = mac or ""
        self.current_mac_label.setText(mac if mac else "(unknown / not available)")

    def on_mac_changed(self, text: str):
        mac = normalize_mac(text)
        ok = is_valid_mac(mac)
        self.valid_label.setText("✓" if ok else "✗")

    def on_random(self):
        self.mac_input.setText(random_mac())

    def on_restore(self):
        iface = self.iface_combo.currentText().strip()
        original = self.original_macs.get(iface, "")
        if original and is_valid_mac(original):
            self.mac_input.setText(original)
        else:
            QMessageBox.warning(self, "Restore unavailable", "No original MAC saved for this interface in this session.")

    def on_apply(self):
        iface = self.iface_combo.currentText().strip()
        mac = normalize_mac(self.mac_input.text())

        if not iface:
            QMessageBox.warning(self, "Missing interface", "Please select an interface.")
            return
        if not is_valid_mac(mac):
            QMessageBox.warning(self, "Invalid MAC", "Use a MAC like: 00:11:22:33:44:55")
            return

        self.append_log(f"[+] Changing MAC for {iface} -> {mac}")
        result = change_mac(iface, mac)
        self.append_log(result.details or result.message)
        self.on_iface_changed(iface)

        if result.ok:
            QMessageBox.information(self, "Success", result.message)
        else:
            QMessageBox.critical(self, "Failed", result.message)

def main():
    app = QApplication(sys.argv)
    w = MacChangerWindow()
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
