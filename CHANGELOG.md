
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
