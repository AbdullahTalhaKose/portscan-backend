{\rtf1\ansi\ansicpg1254\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, request, jsonify\
from flask_cors import CORS\
import socket\
import time\
\
app = Flask(__name__)\
CORS(app)\
\
def port_scan(ip, start_port, end_port):\
    open_ports = []\
    start_time = time.time()\
\
    for port in range(start_port, end_port + 1):\
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\
        s.settimeout(0.2)\
\
        try:\
            s.connect((ip, port))\
            open_ports.append(port)\
        except:\
            pass\
        s.close()\
\
    total_time = round(time.time() - start_time, 3)\
    return \{"open_ports": open_ports, "scan_time": total_time\}\
\
@app.route("/scan", methods=["POST"])\
def scan():\
    data = request.json\
    ip = data["ip"]\
    start_port = int(data["start_port"])\
    end_port = int(data["end_port"])\
    return jsonify(port_scan(ip, start_port, end_port))\
\
@app.route("/")\
def home():\
    return jsonify(\{"message": "PortScan API Running"\})\
}