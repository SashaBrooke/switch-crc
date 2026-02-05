#include <stdio.h>
#include <stdint.h>
#include "crc8_sae_j1850.h"

int main(void)
{
    // D1-D7 in hex
    uint8_t data[7] = { 0x06, 0x02, 0x10, 0x40, 0x00, 0x00, 0x01 };

    // Compute D8 (CRC-8)
    uint8_t d8 = crc8_sae_j1850(data, 7);

    // Print input and CRC
    printf("D1-D7: ");
    for (int i = 0; i < 7; i++)
        printf("0x%02X ", data[i]);
    printf("\nD8 (CRC-8) = 0x%02X\n", d8);

    return 0;
}
