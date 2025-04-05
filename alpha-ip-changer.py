# -*- coding: utf-8 -*-

import time
import os
import subprocess

try:
    import requests
except ImportError:
    print('[+] python3 requests is not installed.')
    os.system('pip3 install requests requests[socks]')
    print('[!] python3 requests installed successfully.')
    import requests

# Check if TOR is installed
try:
    subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:
    print('[+] TOR is not installed!')
    subprocess.check_output('sudo apt update', shell=True)
    subprocess.check_output('sudo apt install tor -y', shell=True)
    print('[!] TOR installed successfully.')

# Clear terminal screen
os.system("clear")

def get_my_ip():
    try:
        url = 'http://checkip.amazonaws.com'
        proxies = {
            'http': 'socks5://127.0.0.1:9050',
            'https': 'socks5://127.0.0.1:9050'
        }
        response = requests.get(url, proxies=proxies, timeout=10)
        return response.text.strip()
    except Exception as e:
        return f"Error fetching IP: {e}"

def change_ip():
    os.system("service tor reload")
    print('[+] Your IP has been changed to:', get_my_ip())

# Display banner
print('''\033[1;32;40m 
           __                  __      __                  __   ___  __     
 /\  |    |__) |__|  /\     | |__)    /  ` |__|  /\  |\ | / _` |__  |__)    
/~~\ |___ |    |  | /~~\    | |       \__, |  | /~~\ | \| \__> |___ |  \    
                                                                                 
from AWAN
''')
print("\033[1;40;31m alpha-0.2-pk@proton.me\n")

# Start TOR service
os.system("service tor start")
time.sleep(3)

print("\033[1;32;40mChange your SOCKS proxy to 127.0.0.1:9050 in your browser/tools\n")

# Get user input
try:
    interval = int(input("[+] Time to wait before changing IP (in seconds) [default=60] >> ") or 60)
    loops = input("[+] How many times do you want to change your IP? [Enter for infinite] >> ") or "0"
    loops = int(loops)

    if loops == 0:
        print("Starting infinite IP rotation. Press Ctrl+C to stop.")
        while True:
            time.sleep(interval)
            change_ip()
    else:
        for _ in range(loops):
            time.sleep(interval)
            change_ip()

except KeyboardInterrupt:
    print("\n[!] IP changer stopped by user.")
except ValueError:
    print("[!] Invalid input. Please enter valid numbers.")
