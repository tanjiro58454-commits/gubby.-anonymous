🟢 Gubby Anonymous

Gubby Anonymous is a Python-based terminal utility that displays public IP address and approximate location information through a proxy connection.

✨ Features

- Python-based terminal interface
- Colored terminal output
- Public IP address lookup
- Approximate city and country display
- Configurable refresh interval
- Connection error handling
- Keyboard interruption support

📱 Platform

- Android with Termux
- Linux environments, including Kali NetHunter

Compatibility depends on the installed Python environment and the availability of the required network services.

🛠️ Requirements

- Python 3
- "requests" Python library
- A compatible proxy service, if proxy-based requests are used
- Internet connectivity

📥 Installation — Termux

Update your Termux packages:

apt update && apt upgrade

Install Python and Git:

apt install python git -y

Clone the repository:

git clone https://github.com/tanjiro58454-commits/gubby.-anonymous.git

Enter the project directory:

cd gubby.-anonymous

Install the Python HTTP library:

python -m pip install requests

▶️ Usage

Inspect the source code before running it:

python gubby.anonymous.py

The script expects a SOCKS5 proxy endpoint at "127.0.0.1:9050". If that endpoint is unavailable, its network requests may fail.

⚠️ Important Notes

- Displayed city and country information is approximate and may not reflect the user's actual physical location.
- An IP lookup service reports the address observed for its request; it does not independently change the device's public IP.
- A proxy application's availability does not guarantee that every application on the device uses that proxy.
- Network connectivity, proxy configuration, and service availability affect results.
- Review the source code before executing scripts from any repository.

⚖️ Disclaimer

This project is provided for educational purposes. Use it responsibly and comply with applicable laws and service terms.

The author makes no guarantee of uninterrupted connectivity, anonymity, or a specific IP address or geographic location.

👨‍💻 Author

The Linux Hacker

GitHub: https://github.com/tanjiro58454-commits
