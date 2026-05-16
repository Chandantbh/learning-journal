# Day 1 — Simple Port Scanner
# This checks if common ports are open on a target server

# Results from scanme.nmap.org:
# Port 22 OPEN  — SSH, remote login service
# Port 80 OPEN  — HTTP, unencrypted web server
# Port 443 CLOSED — no HTTPS running
# Port 8080 CLOSED — no dev/proxy server

import socket

def check_port(host, port):
    s = socket.socket()        # creates a network connection object
    s.settimeout(1)            # stops waiting after 1 second if no response
    try:
        s.connect((host, port))    # tries to connect to the port
        print(f"[OPEN]   Port {port} on {host}")
    except:
        print(f"[CLOSED] Port {port} on {host}")
    finally:
        s.close()              # always close the connection after

target = "scanme.nmap.org"    # legal practice server set up by Nmap team
ports = [22, 80, 443, 8080]   # SSH, HTTP, HTTPS, alternative HTTP

print(f"\nScanning {target}...\n")
for port in ports:
    check_port(target, port)