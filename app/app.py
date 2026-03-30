from flask import Flask, jsonify
import psutil
import datetime
import os

app = Flask(__name__)
START_TIME = datetime.datetime.now()

@app.route("/")
def dashboard():
    return jsonify({
        "service": "Docker Compose Health Dashboard",
        "status": "running",
        "environment": os.getenv("APP_ENV", "development")
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/stats")
def stats():
    uptime = str(datetime.datetime.now() - START_TIME).split(".")[0]
    return jsonify({
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "uptime": uptime,
        "disk_percent": psutil.disk_usage("/").percent
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
