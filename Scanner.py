"""
Network Security Scanner
Developed by: Abdul-Aziz Mohammed Ahmed Naji
Cybersecurity & Networks Student | Google Cloud Certified
"""

import socket
from datetime import datetime

def scan_ports(target, ports):
    print(f"\n[+] Scanning target: {target}")
    print(f"[+] Time started: {datetime.now()}")
    print("-" * 50)

    open_ports = []
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[OPEN] Port {port} is open")
            open_ports.append(port)
        s.close()

    print("-" * 50)
    print(f"[+] Scan completed. {len(open_ports)} open ports found.")
    return open_ports

if __name__ == "__main__":
    target = input("Enter target IP (e.g., 127.0.0.1): ")
    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3306, 8080]
    scan_ports(target, common_ports)
