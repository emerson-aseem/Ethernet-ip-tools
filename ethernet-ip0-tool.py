#!/usr/bin/env python3

def main():
    print("== Ethernet IP Tool ==")
    
    ip_address = input("Enter IP address (e.g. 192.168.1.10): ")
    interface = input("Enter interface name (e.g. eth0): ")
    subnet = input("Enter subnet mask or CIDR (e.g. 255.255.255.0 or /24): ")
    gateway = input("Enter default gateway (optional): ")

    print("\nGenerated Commands:\n")

    # Set IP address
    if '/' in subnet:
        ip_cmd = f"ip addr add {ip_address}{subnet} dev {interface}"
    else:
        ip_cmd = f"ifconfig {interface} {ip_address} netmask {subnet}"

    print(f"Set IP: {ip_cmd}")
    print(f"Bring up interface: ip link set {interface} up")
    if gateway:
        print(f"Add default route: ip route add default via {gateway}")

    print("\nOther useful diagnostics:")
    print(f"ip a show {interface}")
    print(f"ethtool {interface}")
    print(f"ping -c 4 {ip_address}")
    print("arp -a")
    print("route -n")

if __name__ == "__main__":
    main()
