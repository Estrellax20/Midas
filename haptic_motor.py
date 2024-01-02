from machine import I2C, Pin
from time import sleep_ms

# Adres I2C urządzenia Pololu 1638
POLOLU_1638_ADDR = 0x5A

# Inicjalizacja I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

# Funkcja do ustawienia parametrów silnika wibracyjnego
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

# Funkcja do testowania silnika wibracyjnego
def vibrate_haptic_motor():
    seq = 0
    for wave in range(1, 124):
        i2c.writeto(POLOLU_1638_ADDR, bytearray([0x04 + seq, wave]))  # Set waveform
        i2c.writeto(POLOLU_1638_ADDR, bytearray([0x0C, 0x01]))  # Go command
        sleep_ms(800)  # Give it enough time to play waveform effect

        if wave % 8 == 0:
            seq += 1
        if wave % 64 == 0:
            seq = 0

# Inicjalizacja silnika wibracyjnego
setup_haptic_motor()

# Testowanie silnika wibracyjnego
vibrate_haptic_motor()
