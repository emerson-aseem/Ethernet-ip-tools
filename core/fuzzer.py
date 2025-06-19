import socket
import random
import time

EIP_PORT = 44818

# Basic ListIdentity packet
BASE_PACKET = bytes.fromhex(
    '63 00 00 00 00 00 00 00'  # ListIdentity command
)

def mutate_packet(packet: bytes) -> bytes:
    # Randomly mutate a few bytes
    packet = bytearray(packet)
    for _ in range(random.randint(1, 4)):
        index = random.randint(0, len(packet)-1)
        packet[index] = random.randint(0, 255)
    return bytes(packet)

def run_fuzzer():
    ip = input("Target IP: ").strip()
    try:
        for i in range(20):
            mutated = mutate_packet(BASE_PACKET)
            s = socket.socket()
            s.settimeout(2)
            s.connect((ip, EIP_PORT))
            s.send(mutated)
            try:
                data = s.recv(512)
                print(f"[{i}] Response: {data.hex()}")
            except socket.timeout:
                print(f"[{i}] No response (timeout)")
            s.close()
            time.sleep(0.5)
    except Exception as e:
        print(f"[!] Fuzzing error: {e}")
