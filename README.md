# switch-crc

## Overview

This repository provides tools for calculating and validating **SAE J1850 CRC-8** values. The specific use case presented in this repository is for computing the CRC (D8) for 7-byte data segments within CAN frames (D1–D7).

It includes:

- **C implementation** for embedded applications.
- **Python scripts** for quick computation and CSV validation.
- Example **CSV data file** with sample D1–D7 (data) + D8 (CRC) values.
