
# 🔍 LAN Network Scanner

A lightweight Python tool for active device discovery and network reconnaissance on local networks. Built as a hands-on learning project while studying for CompTIA Security+ and TryHackMe SOC Level 1.

---

## 🛠️ Features

- **ARP-based device detection** — identifies all active devices on the local network segment
- **TCP Socket scanning** — compatible with Android/Termux (no root required)
- **Banner grabbing** — retrieves service banners from open ports
- **Wordlist generation** — custom password list generator for security testing
- Clean terminal interface with fast output

---

## 📋 Requirements

- Python 3.x
- No external libraries required for basic scanning

---

## 🚀 Usage

```bash
# Run the network scanner
python escaner.py

# Run the banner grabber
python banner_grabber.py

# Generate a custom wordlist
python generador_claves.py
```

---

## 🎯 What I learned

- How ARP requests work at the network layer
- TCP handshake fundamentals and port scanning techniques
- Banner grabbing as a passive reconnaissance method
- Python socket programming for network tools

---

## ⚠️ Disclaimer

This tool is intended for educational purposes and authorized network testing only. Always ensure you have permission before scanning any network.

---

## 👩‍💻 Author

Built by [@nadiarolave-arch](https://github.com/nadiarolave-arch) as part of a self-directed cybersecurity learning roadmap.
