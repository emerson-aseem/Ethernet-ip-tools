from core import debugger, sniffer, fuzzer

def main():
    print("\n== EtherNet/IP Toolkit ==")
    print("[1] Device Debugger")
    print("[2] Packet Sniffer")
    print("[3] CIP Fuzzer")
    print("[4] Exit")

    choice = input("Select an option: ").strip()

    if choice == '1':
        debugger.run_debugger()
    elif choice == '2':
        sniffer.run_sniffer()
    elif choice == '3':
        fuzzer.run_fuzzer()
    elif choice == '4':
        exit(0)
    else:
        print("Invalid choice")

if __name__ == '__main__':
    main()
