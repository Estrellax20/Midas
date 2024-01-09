from machine import I2C, Pin
from time import sleep_ms

I2C_SDA_PIN = 0
I2C_SCL_PIN = 1
ADR = 0x5A
MEM1 = 0x01
BUF1 = 0x00
i2c=I2C(0,sda=Pin(I2C_SDA_PIN), scl=Pin(I2C_SCL_PIN), freq=400000)


#i2c.writeto_mem(int(ADR),  int(mem1),  bytes([int(buf1)]))
def vibration():
    #reg_write(i2c, 0x5A, 0x01, 0x00)  # set mode
    i2c.writeto_mem(int(0x5A), int(0x01), '0') # set mode
    #reg_write(i2c, 0x1A, 0x36) # motor select
    #reg_write(i2c, 0x5A, 0x1A, 0x55) # motor select
    i2c.writeto_mem(int(0x5A), int(0x1A), bytes([int(0x55)])) # motor select
    #reg_write(i2c, 0x5A, 0x03, 0x02)  # set library
    i2c.writeto_mem(int(0x5A), int(0x03), bytes([int(0x02)])) # set library

    i2c.writeto_mem(int(0x5A), int(0x04), bytes([int(0x01)]))  # Set waveform, can be changed -> 0x01

    i2c.writeto_mem(int(0x5A), int(0x0C), bytes([int(0x01)])) # Go command

#data = bytes[]
#i2c.readfrom_mem_into(0x5A, 0x00, data)
#status = i2c.read(i2c, 0x5A, 0x00, 0x00)

#data = bytearray(2)
#i2c.readfrom_mem_into(0x5A, 0x00, data)
#print(data)
#print(hex(data))