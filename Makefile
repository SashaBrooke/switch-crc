# Compiler
CC = gcc

# Compiler flags
CFLAGS = -Wall -Wextra -O2

# Target executable
TARGET = test_crc

# Source files
SRC = test_crc.c crc8_sae_j1850.c

# Default rule
all: $(TARGET)

# Build the executable
$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC)

# Clean up
clean:
	rm -f $(TARGET)
