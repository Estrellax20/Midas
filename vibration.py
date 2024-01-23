from machine import I2C, Pin
from time import sleep_ms

I2C_SDA_PIN = 10
I2C_SCL_PIN = 11
ADR = 0x5A
MEM1 = 0x01
BUF1 = 0x00
SOFT_GND_PIN = Pin(9, mode=Pin.OUT, value=0)
SOFT_IN_PIN = Pin(12, mode=Pin.OUT, value=0)
#SOFT_VNC_PIN = Pin(7, mode=Pin.OUT, value=1)
EN_PIN = Pin(13, mode=Pin.OUT, value=1)
i2c2=I2C(1,sda=Pin(I2C_SDA_PIN), scl=Pin(I2C_SCL_PIN), freq=400000)

def vibration():
    #reg_write(i2c, 0x5A, 0x01, 0x00)  # set mode
    i2c2.writeto_mem(int(0x5A), int(0x01), '0') # set mode
    #reg_write(i2c, 0x1A, 0x36) # motor select
    #reg_write(i2c, 0x5A, 0x1A, 0x55) # motor select
    i2c2.writeto_mem(int(0x5A), int(0x1A), bytes([int(0x55)])) # motor select
    #reg_write(i2c, 0x5A, 0x03, 0x02)  # set library
    i2c2.writeto_mem(int(0x5A), int(0x03), bytes([int(0x02)])) # set library

    i2c2.writeto_mem(int(0x5A), int(0x04), bytes([int(0x01)]))  # Set waveform, can be changed -> 0x01

    i2c2.writeto_mem(int(0x5A), int(0x0C), bytes([int(0x01)])) # Go command


def vibration_test():
    print("Vibration test!")
    while 1:
        vibration()
        sleep_ms(500)

if __name__ == "__main__":
    SOFT_GND_PIN = Pin(2, mode=Pin.OUT, value=0)
    SOFT_VNC_PIN = Pin(3, mode=Pin.OUT, value=1)
    vibration_test()
    
