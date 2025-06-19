from scapy.all import sniff, TCP, UDP, IP, Raw

EIP_PORTS = [44818, 2222]

def process_packet(pkt):
    if Raw in pkt and IP in pkt:
        raw = pkt[Raw].load
        print("\n[+] Packet:")
        print(f"From {pkt[IP].src}:{pkt[TCP].sport if TCP in pkt else pkt[UDP].sport}")
        print(f"To   {pkt[IP].dst}:{pkt[TCP].dport if TCP in pkt else pkt[UDP].dport}")
        print(f"Payload: {raw.hex()}")

def run_sniffer():
    iface = input("Enter interface (e.g., eth0): ").strip()
    print(f"[*] Sniffing on {iface}... (EIP ports)")
    sniff(filter="tcp port 44818 or udp port 2222", iface=iface, prn=process_packet, store=False)
