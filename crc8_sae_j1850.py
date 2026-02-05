def crc8_sae_j1850(data):
    crc = 0xFF
    poly = 0x1D

    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x80:
                crc = ((crc << 1) ^ poly) & 0xFF
            else:
                crc = (crc << 1) & 0xFF

    return crc ^ 0xFF


# =========================
# PUT YOUR D1–D7 BYTES HERE
# =========================
D1_to_D7 = [
    0x06,  # D1
    0x03,  # D2
    0x10,  # D3
    0x38,  # D4
    0x00,  # D5
    0x00,  # D6
    0x0A,  # D7
]

# Compute and print D8
d8 = crc8_sae_j1850(D1_to_D7)
print(f"Expected D8 (CRC): 0x{d8:02X}")
