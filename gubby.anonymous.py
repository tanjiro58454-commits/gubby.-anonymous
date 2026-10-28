#!/usr/bin/env python3
import time
import os
import sys
import requests

# Terminal colors for styling
RED   = "\033[1;31m"
GREEN = "\033[1;32m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

# Tor SOCKS5 Proxy config
proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

def display_banner():
    os.system('clear')
    print(f"{CYAN}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{RESET}")
    print(f"{GREEN}██████   ██    ██  ██████  ██████  ██    ██ ██     ██")
    print("██       ██    ██  ██   ██ ██   ██  ██  ██   ██   ██ ")
    print("██   ███ ██    ██  ██████  ██████    ████     ██ ██  ")
    print("██    ██ ██    ██  ██   ██ ██   ██    ██       ██    ")
    print(f"████████  ██████   ██████  ██████     ██       ██    {RED}[v2.0]{GREEN}")
    print(f"{CYAN}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{RESET}")
    print(f"{BLUE}      █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
    print(f"      █   {RESET}{GREEN}GUBBY ANONYMOUS IP ROTATOR{RESET}{BLUE}       █")
    print(f"      █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{RESET}\n")

def get_ip_details():
    try:
        # IP, Country aur City fetch karne ke liye standard API
        response = requests.get('https://ipapi.co', proxies=proxies, timeout=5)
        data = response.json()
        ip = data.get('ip', 'Unknown')
        country = data.get('country_name', 'Unknown')
        city = data.get('city', 'Unknown')
        return ip, country, city
    except Exception:
        return None, None, None

def change_ip():
    # Tor ko signal bhejna naya path (circuit) banane ke liye
    os.system("pkill -HUP tor")

def main():
    display_banner()
    
    print(f"[*] Starting Tor core service...")
    os.system("service tor start > /dev/null 2>&1 || tor > /dev/null 2>&1 &")
    time.sleep(4) # Initial connection time

    try:
        refresh_time = int(input(f"[?] Enter IP rotation interval (in seconds): "))
        if refresh_time < 2:
            refresh_time = 2  # Circuit switch hone mein thoda time lagta hai
    except ValueError:
        print(f"{RED}[!] Invalid input. Defaulting to 5 seconds.{RESET}")
        refresh_time = 5

    print(f"\n{GREEN}[+] Tool Active! Tracking jumps... Press Ctrl+C to Stop.{RESET}\n")
    print(f"{YELLOW}[*] Establishing first secure proxy tunnel...{RESET}")
    
    ip_count = 0
    
    try:
        while True:
            ip, country, city = get_ip_details()
            
            if ip:
                ip_count += 1
                print(f"{CYAN}" + "-"*50)
                print(f"{GREEN}[SUCCESS] Jump Count: #{ip_count}{RESET}")
                print(f"[#] Connected via: {YELLOW}{city}, {country}{RESET}")
                print(f"[#] Public IP: {GREEN}{ip}{RESET}")
                print(f"{CYAN}" + "-"*50 + f"{RESET}")
            else:
                print(f"{RED}[!] Network hop delay. Retrying circuit connection...{RESET}")
            
            time.sleep(refresh_time)
            
            print(f"\n[*] Requesting new server identity from Tor network...")
            change_ip()
            time.sleep(2.5) # Tor ko naya path build karne ka time dena
            
    except KeyboardInterrupt:
        print(f"\n\n{RED}[-] Gubby.Anonymous Stopped. Total IP Jumps: {ip_count}{RESET}\n")

if __name__ == "__main__":
    main()

