import csv
import sys


def crc8_sae_j1850(data):
    """
    CRC-8 SAE J1850
    poly = 0x1D
    init = 0xFF
    xorout = 0xFF
    no reflection
    """
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


def parse_hex(value):
    """
    Parse CSV byte value as hex (e.g. '6', '10', '40', 'FF')
    """
    return int(value.strip(), 16)


def main(csv_path):
    mismatches = 0

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row_num, row in enumerate(reader, start=2):
            d = [
                parse_hex(row["D1"]),
                parse_hex(row["D2"]),
                parse_hex(row["D3"]),
                parse_hex(row["D4"]),
                parse_hex(row["D5"]),
                parse_hex(row["D6"]),
                parse_hex(row["D7"]),
            ]

            actual_d8 = parse_hex(row["D8"])
            expected_d8 = crc8_sae_j1850(d)

            if actual_d8 != expected_d8:
                mismatches += 1
                d_str = " ".join(f"{b:02X}" for b in d)
                print(
                    f"Row {row_num}: "
                    f"D1-7=[{d_str}] "
                    f"Actual D8=0x{actual_d8:02X} "
                    f"Expected D8=0x{expected_d8:02X}"
                )
            else:
                print(f"Row {row_num}: expected D8=0x{expected_d8:02X} matches actual D8=0x{actual_d8:02X}")

    print(f"\nDone. Total mismatches: {mismatches}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python csv_check__crc8_sae_j1850.py <input.csv>")
        sys.exit(1)

    main(sys.argv[1])
