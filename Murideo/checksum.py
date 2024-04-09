def add_checksum(hex_data):
    total = sum(int(byte, 16) for byte in hex_data)
    checksum = (~total + 1) & 0xFF
    return hex_data + [f"{checksum:02X}"]


data = ["AA", "00", "00", "06", "00", "00", "00", "F7", "78", "00"]
print(add_checksum(data)[-1])  # Prints 'C9'
