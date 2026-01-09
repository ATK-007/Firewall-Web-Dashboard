import socket
import struct
import sqlite3
from datetime import datetime

DB = "traffic.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS traffic (
            time TEXT,
            src_ip TEXT
        )
    """)
    conn.commit()
    conn.close()

def get_src_ip(packet):
    ip_header = packet[14:34]
    src = struct.unpack("!12x4s", ip_header)[0]
    return socket.inet_ntoa(src)

def main():
    init_db()
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    print("📡 Traffic Sniffer Started...")

    while True:
        raw, _ = conn.recvfrom(65536)
        if raw[12:14] == b'\x08\x00':  # IPv4
            src_ip = get_src_ip(raw)
            t = datetime.now().strftime("%H:%M:%S")

            db = sqlite3.connect(DB)
            c = db.cursor()
            c.execute("INSERT INTO traffic VALUES (?,?)", (t, src_ip))
            db.commit()
            db.close()

if __name__ == "__main__":
    main()
