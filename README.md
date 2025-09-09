# Nmap Multitool 🛠️

```
·▄▄▄▄   ▄▄▄·  ▐ ▄        ▐ ▄ ▄▄▄ .▄ •▄     • ▌ ▄ ·. ▄• ▄▌▄▄▌  ▄▄▄▄▄▪  ▄▄▄▄▄            ▄▄▌  
██▪ ██ ▐█ ▀█ •█▌▐█▪     •█▌▐█▀▄.▀·█▌▄▌▪    ·██ ▐███▪█▪██▌██•  •██  ██ •██  ▪     ▪     ██•  
▐█· ▐█▌▄█▀▀█ ▐█▐▐▌ ▄█▀▄ ▐█▐▐▌▐▀▀▪▄▐▀▀▄·    ▐█ ▌▐▌▐█·█▌▐█▌██▪   ▐█.▪▐█· ▐█.▪ ▄█▀▄  ▄█▀▄ ██▪  
██. ██ ▐█ ▪▐▌██▐█▌▐█▌.▐▌██▐█▌▐█▄▄▌▐█.█▌    ██ ██▌▐█▌▐█▄█▌▐█▌▐▌ ▐█▌·▐█▌ ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌
▀▀▀▀▀•  ▀  ▀ ▀▀ █▪ ▀█▄▀▪▀▀ █▪ ▀▀▀ ·▀  ▀    ▀▀  █▪▀▀▀ ▀▀▀ .▀▀▀  ▀▀▀ ▀▀▀ ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀ 

```

A sleek, badass command-line tool for running Nmap scans like a pro. This Python-based multitool lets you fire off various Nmap scans through an interactive menu, complete with IP validation and a slick ASCII art vibe. Whether you're a network ninja or just dipping your toes into security testing, this tool makes scanning fast, fun, and reliable. 😎

## Features
- **Interactive Menu**: Choose from predefined Nmap scan types with ease.
- **Scan Options**:
  - Fast scan (`-T4 -F`)
  - Full port scan with version detection (`-p- -sV`)
  - OS detection (`-O`)
  - Aggressive scan with output saving (`-A -oA scan`)
- **IP Validation**: No more invalid IP nonsense – only legit addresses allowed.
- **Modular Design**: Scan options are stored in a separate file (`scan_options.py` or `scan_options.json`) for clean code.
- **Error Handling**: Gracefully handles missing Nmap, invalid inputs, or scan errors.


## Installation
1. **Clone the repo**:
   ```bash
   git clone https://github.com/yourusername/nmap-multitool.git
   cd nmap-multitool
   ```
2. **Install Nmap** (if not already installed):
   ```bash
   sudo apt update && sudo apt install nmap
   ```
3. **Ensure Python 3 is installed** (usually pre-installed on Kali Linux):
   ```bash
   python3 --version
   ```
4. **Optional (JSON version)**: If using the JSON config, ensure the `json` module is available (included in Python standard library).

## Usage
1. Run the tool:
   ```bash
   python3 main.py
   ```
2. Select `1` for Nmap scans or `2` to exit.
3. Choose a scan type (1-4) from the menu.
4. Enter a valid IP address (e.g., `127.0.0.1`).
5. Watch the magic happen as Nmap results roll in! 😎

## Example
```bash
$ python3 main.py

·▄▄▄▄ ▄▄▄· ▐ ▄ ▐ ▄ ▄▄▄ .▄ •▄ • ▌ ▄ ·. ▄• ▄▌▄▄▌ ▄▄▄▄▄▪ ▄▄▄▄▄ ▄▄▌
██▪ ██ ▐█ ▀█ •█▌▐█▪ •█▌▐█▀▄.▀·█▌▄▌▪ ·██ ▐███▪█▪██▌██• •██ ██ •██ ▪ ▪ ██•
▐█· ▐█▌▄█▀▀█ ▐█▐▐▌ ▄█▀▄ ▐█▐▐▌▐▀▀▪▄▐▀▀▄· ▐█ ▌▐▌▐█·█▌▐█▌██▪ ▐█.▪▐█· ▐█.▪ ▄█▀▄ ▄█▀▄ ██▪
██. ██ ▐█ ▪▐▌██▐█▌▐█▌.▐▌██▐█▌▐█▄▄▌▐█.█▌ ██ ██▌▐█▌▐█▄█▌▐█▌▐▌ ▐█▌·▐█▌ ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌
▀▀▀▀▀• ▀ ▀ ▀▀ █▪ ▀█▄▀▪▀▀ █▪ ▀▀▀ ·▀ ▀ ▀▀ █▪▀▀▀ ▀▀▀ .▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀█▄▀▪ ▀█▄▀▪.▀▀▀

=== MENU ===
1. nmap
2. exit

> 1
1. fast scan (nmap -T4 -F)
2. full scan (nmap -p- -sV)
3. flag scan (nmap -O)


> 1
Type an IP address: > 127.0.0.1

=== Nmap Scan Results ===
Starting Nmap 7.94 ( https://nmap.org ) at 2025-09-09 23:04 CEST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.0001s latency).
Not shown: 97 closed ports
PORT    STATE SERVICE
22/tcp  open  ssh
80/tcp  open  http
443/tcp open  https
Nmap done: 1 IP address (1 host up) scanned in 0.05 seconds
```

## Configuration
Scan options are stored in a separate file for easy customization:
- **Python version**: Edit `scan_options.py` to add or modify scan types.
- **JSON version**: Edit `scan_options.json` for a more standard config format.

Example (`scan_options.py`):
```python
scan_options = [
    {"id": "1", "name": "fast scan", "flags": "-T4 -F"},
    {"id": "2", "name": "full scan", "flags": "-p- -sV"},
    {"id": "3", "name": "flag scan", "flags": "-O"}
]
```

To add a new scan, append a new dictionary to the list with `id`, `name`, and `flags`.

## Requirements
- Python 3.x
- Nmap (`sudo apt install nmap`)
- Python modules: `ipaddress`, `subprocess` (built-in), `json` (for JSON config)

## Disclaimer
⚠️ **Use responsibly!** Network scanning without permission is illegal. Only scan networks or devices you own or have explicit authorization to test.

## Contributing
Got ideas to make this tool even more badass? Submit a pull request or open an issue! Let’s build something epic together, mordzia! 💪

## License
This project is licensed under a modified MIT License with an ASCII Art Protection Clause.
You are free to use, modify, and distribute the code, but the ASCII art logo must remain unchanged. See the LICENSE file for details.

---

**Cya in the cyberworld, mordzia! 😎**
