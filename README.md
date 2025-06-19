# Ethernet IP Tool

A simple command-line tool to assist with Ethernet IP configuration and diagnostics.

## Features

- Prompts for:
  - IP address
  - Network interface
  - Subnet/CIDR
  - Gateway (optional)
- Generates:
  - Commands to set IP and bring interface up
  - Common networking tools: `ip`, `ethtool`, `ping`, `arp`, etc.

## Usage

```bash
pip install -r requirements.txt
python3 ethernet_ip_tool.py
