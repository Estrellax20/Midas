from machine import I2C, Pin
from time import sleep_ms

# I2C address of the Pololu 1638 device
POLOLU_1638_ADDR = 0x5A

# Initializing I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

# Function to set parameters for the haptic motor
def setup_haptic_motor():
    # Set mode to internal trigger input
    i2c.writeto(POLOLU_1638_ADDR, bytearray([0x01, 0x09]))

    # Select LRA motor
    i2c.writeto(POLOLU_1638_ADDR, bytearray([0x03, 0b110111]))

    # Select ERM library
    i2c.writeto(POLOLU_1638_ADDR, bytearray([0x05, 0x02]))

    # Get status
    status = i2c.readfrom(POLOLU_1638_ADDR, 1)
    print("Status:", status[0])

# Function to test the haptic motor
def vibrate_haptic_motor():
    seq = 0
    for wave in range(1, 124):
        i2c.writeto(POLOLU_1638_ADDR, bytearray([0x04 + seq, wave]))  # Set waveform
        i2c.writeto(POLOLU_1638_ADDR, bytearray([0x0C, 0x01]))  # Go command
        sleep_ms(800)

        if wave % 8 == 0:
            seq += 1
        if wave % 64 == 0:
            seq = 0

# Initializing the haptic motor
setup_haptic_motor()

# Testing the haptic motor
vibrate_haptic_motor()
