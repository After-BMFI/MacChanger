#Build script (creates a Linux binary)
#!/usr/bin/env bash
set -e

# Build on Linux with Python 3.9–3.12
python3 -V

python3 -m pip install --upgrade pip
python3 -m pip install PySide6 psutil pyinstaller

# Clean old builds
rm -rf build dist MacChanger.spec

# Build one-file binary
pyinstaller --onefile --name MacChanger macchanger_gui.py

echo ""
echo "Built binary: dist/MacChanger"
