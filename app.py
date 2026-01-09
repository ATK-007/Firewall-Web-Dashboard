from flask import Flask, render_template, jsonify, request
import sqlite3
from firewall_control import allow_ip, block_ip

app = Flask(__name__)
DB = "traffic.db"

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/traffic")
def traffic_data():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        SELECT time, COUNT(*) 
        FROM traffic 
        GROUP BY time 
        ORDER BY time DESC 
        LIMIT 10
    """)
    rows = c.fetchall()
    conn.close()

    rows.reverse()
    return jsonify({
        "labels": [r[0] for r in rows],
        "data": [r[1] for r in rows]
    })

@app.route("/api/block", methods=["POST"])
def block():
    ip = request.json.get("ip")
    if ip:
        block_ip(ip)
        return jsonify({"status": "blocked", "ip": ip})
    return jsonify({"error": "IP missing"}), 400

@app.route("/api/allow", methods=["POST"])
def allow():
    ip = request.json.get("ip")
    if ip:
        allow_ip(ip)
        return jsonify({"status": "allowed", "ip": ip})
    return jsonify({"error": "IP missing"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
