# macchanger_core.py (Linux-first, Kali compatible + fallback)
#!/usr/bin/env python3
import os
import platform
import random
import re
import shutil
import subprocess
from dataclasses import dataclass

MAC_REGEX = re.compile(r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$")

def normalize_mac(mac: str) -> str:
    return mac.strip().lower().replace("-", ":")

def is_valid_mac(mac: str) -> bool:
    return bool(MAC_REGEX.match(mac))

def is_root_linux() -> bool:
    return hasattr(os, "geteuid") and os.geteuid() == 0

def which(cmd: str) -> bool:
    return shutil.which(cmd) is not None

@dataclass
class ChangeResult:
    ok: bool
    message: str
    details: str = ""

def run_cmd(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, text=True, capture_output=True)

def random_mac(local_admin: bool = True) -> str:
    first = random.randint(0x00, 0xFF)
    if local_admin:
        first = (first | 0x02) & 0xFE
    mac = [first] + [random.randint(0x00, 0xFF) for _ in range(5)]
    return ":".join(f"{b:02x}" for b in mac)

def change_mac_linux(interface: str, new_mac: str) -> ChangeResult:
    if not is_root_linux():
        return ChangeResult(
            ok=False,
            message="Permission denied. Please run with admin privileges (pkexec/sudo).",
            details="Linux requires root privileges to change MAC addresses.",
        )

    new_mac = normalize_mac(new_mac)
    logs = []

    # Preferred: iproute2
    if which("ip"):
        cmds = [
            ["ip", "link", "set", "dev", interface, "down"],
            ["ip", "link", "set", "dev", interface, "address", new_mac],
            ["ip", "link", "set", "dev", interface, "up"],
        ]
        for cmd in cmds:
            p = run_cmd(cmd)
            logs.append(f"$ {' '.join(cmd)}\n{(p.stdout or '')}{(p.stderr or '')}".strip())
            if p.returncode != 0:
                return ChangeResult(False, "MAC change failed (ip).", "\n\n".join(logs))
        return ChangeResult(True, "MAC address changed (ip).", "\n\n".join(logs))

    # Fallback: ifconfig (net-tools)
    if which("ifconfig"):
        cmds = [
            ["ifconfig", interface, "down"],
            ["ifconfig", interface, "hw", "ether", new_mac],
            ["ifconfig", interface, "up"],
        ]
        for cmd in cmds:
            p = run_cmd(cmd)
            logs.append(f"$ {' '.join(cmd)}\n{(p.stdout or '')}{(p.stderr or '')}".strip())
            if p.returncode != 0:
                return ChangeResult(False, "MAC change failed (ifconfig).", "\n\n".join(logs))
        return ChangeResult(True, "MAC address changed (ifconfig).", "\n\n".join(logs))

    return ChangeResult(
        ok=False,
        message="No supported tool found: install iproute2 (ip) or net-tools (ifconfig).",
        details="Kali/Debian: sudo apt install iproute2",
    )

def change_mac_windows(interface: str, new_mac: str) -> ChangeResult:
    # Driver-dependent; included for completeness
    mac_no_sep = normalize_mac(new_mac).replace(":", "").upper()
    ps = f"""
    $ErrorActionPreference='Stop';
    $name = "{interface}";
    $val = "{mac_no_sep}";
    Set-NetAdapterAdvancedProperty -Name $name -RegistryKeyword "NetworkAddress" -RegistryValue $val -NoRestart:$true;
    Disable-NetAdapter -Name $name -Confirm:$false;
    Start-Sleep -Seconds 2;
    Enable-NetAdapter -Name $name -Confirm:$false;
    "OK";
    """.strip()

    cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps]
    p = run_cmd(cmd)
    details = f"$ powershell\n{(p.stdout or '')}{(p.stderr or '')}".strip()

    if p.returncode != 0:
        return ChangeResult(False, "Windows MAC change failed (Admin required; adapter may not support it).", details)
    return ChangeResult(True, "Windows MAC change attempted (driver-dependent).", details)

def change_mac(interface: str, new_mac: str) -> ChangeResult:
    interface = (interface or "").strip()
    new_mac = normalize_mac(new_mac)

    if not interface:
        return ChangeResult(False, "Interface is required.")
    if not is_valid_mac(new_mac):
        return ChangeResult(False, "Invalid MAC format (00:11:22:33:44:55).")

    system = platform.system().lower()
    if system == "linux":
        return change_mac_linux(interface, new_mac)
    if system == "windows":
        return change_mac_windows(interface, new_mac)

    return ChangeResult(False, f"Unsupported OS: {platform.system()}")
