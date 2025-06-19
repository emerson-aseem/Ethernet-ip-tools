# EtherNet/IP Toolkit

A modular toolkit for debugging, sniffing, and fuzzing EtherNet/IP (EIP) traffic.

## Features

- 📡 Device Debugger using `pycomm3`
- 🔍 Live Packet Sniffer using `scapy`
- 💣 CIP Fuzzer for robustness testing

## Usage

```bash
pip install -r requirements.txt
python3 main.py
```

## Modes

### 1. Device Debugger
Retrieve basic device information using the CIP RegisterSession.

### 2. Packet Sniffer
Capture live EIP packets on TCP/44818 and UDP/2222.

### 3. Fuzzer
Send random or malformed EIP packets to test robustness.

## Ethical Usage
This toolkit is for research and educational use only. Do **not** use it on networks or devices without explicit permission.

## License
MIT
