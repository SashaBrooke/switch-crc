// ===============================
// Constants
// ===============================

const CRC_PLACEHOLDER = 0x00;

// SAE J1850 CRC-8 parameters
const CRC_POLY = 0x1D;
const CRC_INIT = 0xFF;
const CRC_XOR_OUT = 0xFF;


// ===============================
// CRC implementation (bitwise)
// ===============================

function crc8_sae_j1850(bytes) {
    let crc = CRC_INIT;

    for (let byte of bytes) {
        crc ^= byte;

        for (let i = 0; i < 8; i++) {
            if (crc & 0x80) {
                crc = ((crc << 1) ^ CRC_POLY) & 0xFF;
            } else {
                crc = (crc << 1) & 0xFF;
            }
        }
    }

    return crc ^ CRC_XOR_OUT;
}


// ===============================
// Update D8 in-place
// ===============================

function updateCRC8(frame) {
    if (frame.length !== 8) {
        throw new Error("Frame must be 8 bytes (D1-D8)");
    }

    const crc = crc8_sae_j1850(frame.slice(0, 7));
    frame[7] = crc;
}


// ===============================
// Utils
// ===============================

function formatHex(byte) {
    return byte.toString(16).toUpperCase().padStart(2, '0');
}



// ===============================
// Example usage
// ===============================

let tx0 = [];

tx0[0] = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0E, CRC_PLACEHOLDER];

updateCRC8(tx0[0]);

console.log("Frame with CRC: [", tx0[0].map(formatHex).join(' '), "]");
