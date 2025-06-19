from pycomm3 import CIPDriver

def run_debugger():
    ip = input("Enter target IP: ").strip()

    try:
        with CIPDriver(ip) as plc:
            print(f"\n[✓] Connected to {ip}")
            info = plc.device_info
            for k, v in info.items():
                print(f"{k.title().replace('_', ' ')}: {v}")
    except Exception as e:
        print(f"[!] Failed to connect or retrieve info: {e}")
