/**
 * @file crc8_sae_j1850.h
 * @brief SAE J1850 CRC-8 calculation.
 *
 * This module provides functionality to calculate the SAE J1850 CRC-8 for
 * a given data buffer. This implementation uses a precomputed lookup table
 * for speed.
 */

#ifndef CRC8_SAE_J1850_H
#define CRC8_SAE_J1850_H

#include <stdint.h>

/**
 * @brief Compute SAE J1850 CRC-8 for a data buffer.
 *
 * @param data Pointer to the data buffer.
 * @param len  Length of the data buffer in bytes.
 * @return CRC-8 value (uint8_t) to append to the message.
 */
uint8_t crc8_sae_j1850(const uint8_t* data, unsigned int len);

#endif // CRC8_SAE_J1850_H
