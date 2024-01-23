from machine import I2C, Pin
from time import sleep_ms

#I2C_SDA_PIN = 6
#I2C_SCL_PIN = 7
#ADR = 0x5A
#MEM1 = 0x01
#BUF1 = 0x00
#i2c=I2C(1,sda=Pin(I2C_SDA_PIN), scl=Pin(I2C_SCL_PIN), freq=400000)


#SOFT_VNC_PIN = Pin(5, mode=Pin.OUT, value=1)


I2C_SDA_PIN = 4
I2C_SCL_PIN = 5
ADR = 0x5A
MEM1 = 0x01
BUF1 = 0x00
SOFT_GND_PIN = Pin(2, mode=Pin.OUT, value=0)
SOFT_VNC_PIN = Pin(3, mode=Pin.OUT, value=1)
EN_PIN = Pin(6, mode=Pin.OUT, value=1)
i2c=I2C(0,sda=Pin(I2C_SDA_PIN), scl=Pin(I2C_SCL_PIN), freq=400000)

# sda=machine.Pin(4)
# scl=machine.Pin(5)
# i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)

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


def vibration_test():
    print("Vibration test!")
    while 1:
        vibration()
        sleep_ms(500)

if __name__ == "__main__":
    SOFT_GND_PIN = Pin(2, mode=Pin.OUT, value=0)
    SOFT_VNC_PIN = Pin(3, mode=Pin.OUT, value=1)
    vibration_test()
   
#while(1):
#    SOFT_GND_PIN = Pin(4, mode=Pin.OUT, value=0)
#    SOFT_VNC_PIN = Pin(5, mode=Pin.OUT, value=1)
#    EN_PIN = Pin(9, mode=Pin.OUT, value=1)
#    print('Vibru')
#    vibration()
    
