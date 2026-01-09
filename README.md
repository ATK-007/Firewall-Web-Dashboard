# 🌐 Firewall Web Dashboard with Real-Time Traffic Graphs

A cybersecurity project that provides:
- Real-time network traffic monitoring
- Live traffic graphs using Chart.js
- Firewall allow/block via web interface
- Linux UFW integration

## 🚀 Features
- Flask web dashboard
- Packet sniffing using raw sockets
- SQLite traffic storage
- Real-time graphs
- Firewall control APIs

## ▶️ How to Run

```bash
sudo ufw enable
sudo python3 traffic_sniffer.py
sudo python3 app.py
Open browser:
http://localhost:5000


---

# 8️⃣ `traffic.db`
👉 **DO NOT create manually**  
It is **auto-created** when you run:
```bash
sudo python3 traffic_sniffer.py


👨‍💻 Author

Ashish Atmakuri
Cybersecurity Enthusiast

FINAL RUN ORDER:
sudo ufw enable
sudo python3 traffic_sniffer.py
# open NEW terminal
sudo python3 app.py

Then open:

http://localhost:5000
