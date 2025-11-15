from flask import Flask, request, jsonify
from flask_cors import CORS
import socket
import time

app = Flask(__name__)
CORS(app)

def port_scan(ip, start_port, end_port):
    open_ports = []
    start_time = time.time()

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.2)

        try:
            s.connect((ip, port))
            open_ports.append(port)
        except:
            pass

        s.close()

    total_time = round(time.time() - start_time, 3)

    return {
        "open_ports": open_ports,
        "scan_time": total_time
    }


@app.route("/scan", methods=["POST"])
def scan():
    data = request.json

    ip = data.get("ip")
    start_port = int(data.get("start_port"))
    end_port = int(data.get("end_port"))

    result = port_scan(ip, start_port, end_port)

    return jsonify(result)


@app.route("/")
def home():
    return jsonify({"message": "PortScanLite Backend Running"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
