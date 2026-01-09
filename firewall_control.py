import os

def allow_ip(ip):
    os.system(f"sudo ufw allow from {ip}")

def block_ip(ip):
    os.system(f"sudo ufw deny from {ip}")

def allow_port(port):
    os.system(f"sudo ufw allow {port}")

def block_port(port):
    os.system(f"sudo ufw deny {port}")
