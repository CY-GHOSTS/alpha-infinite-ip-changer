# alpha-infinite-ip-changer
A lightweight Python script to automatically change your TOR exit IP address at set intervals. Useful for privacy, scraping, penetration testing, or any task that benefits from rotating IPs — all from the command line.

# 🧅 Alpha Infinite IP Changer

A lightweight Python-based TOR IP auto-changer script that automatically rotates your public IP address through the TOR network at regular intervals. Built for privacy-conscious users, penetration testers, and developers who need to maintain anonymity or bypass IP-based restrictions.

> **Author**: CY-GHOSTS  
> **Contact**: [alpha-0.2-pk@proton.me](mailto:alpha-0.2-pk@proton.me)

---

## ⚙️ Features

- 🔁 Infinite or timed TOR IP rotation
- 🌐 Detects and displays current IP
- 🔒 Uses TOR's SOCKS5 proxy (127.0.0.1:9050)
- 📦 Automatically installs missing dependencies (`requests`)
- ✅ Works on **Linux**, **Termux (Android)**, and most UNIX-based systems

---

## 📸 Preview

![Preview](https://user-images.githubusercontent.com/your-screenshot.png)
<!-- Replace this with an actual screenshot later if you want -->

---

## 🖥️ Linux Installation & Usage

### 🔧 Requirements

- Python 3
- TOR
- `requests` Python module with SOCKS support

### 📥 Install Dependencies

```bash
sudo apt update && sudo apt install tor python3 -y
pip3 install requests[socks]
git clone https://github.com/CY-GHOSTS/alpha-infinite-ip-changer
ls
chmod +x alpha-ip-changer.py
ls
cd alpha-ip-changer.py
python alpha-ip-changer.py

