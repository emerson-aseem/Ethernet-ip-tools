#!/usr/bin/env python3

from pycomm3 import CIPDriver
import sys

def main():
    print("== EtherNet/IP Tool ==")

    ip = input("Enter target device IP address: ").strip()

    try:
        with CIPDriver(ip) as plc:
            print(f"\n[✓] Connected to {ip}")
            print(f"Product Name: {plc.device_info.get('product_name')}")
            print(f"Vendor: {plc.device_info.get('vendor')}")
            print(f"Serial: {plc.device_info.get('serial_number')}")
            print(f"Device Type: {plc.device_info.get('device_type')}")

            print("\n--- Common CIP Attributes ---")
            print(f"Status: {plc.device_info.get('status')}")
            print(f"Revision: {plc.device_info.get('revision')}")
            print(f"State: {plc.device_info.get('state')}")

    except Exception as e:
        print(f"[!] Failed to connect or fetch info: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
