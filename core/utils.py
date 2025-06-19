def parse_hex_dump(data):
    return ' '.join(f'{b:02x}' for b in data)
