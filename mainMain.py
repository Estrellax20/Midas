import network
import ubinascii
import urequests as requests
import time
from config import *
import machine
from lib.icm20948 import *
import socket
import random
from adc import *
from lib.neopixel import Neopixel
from vibration import *
from lib.buzzer import *

print('Initialize')
playsong(mario)
icm20948=ICM20948()

button = 0

# Initialize the Neopixel object to control RGB LED lights
strip = Neopixel(1, 0, LED_PIN, "GRB")
# Set the brightness of the LED lights to the value defined as LED_BRIGHTNESS
strip.brightness(LED_BRIGHTNESS)
strip.fill(LED_COLORS['yellow'])
strip.show()
print('Initialize sucessful')
strip.fill(LED_COLORS['green'])
strip.show()

while (True):
    button = adc_scaled()
 
    if button > 3000:
        print('Button pressed')
        strip.fill(LED_COLORS['blue'])
        strip.show()
        vibration()
        playtone(392)
    else:
        strip.fill(LED_COLORS['green'])
        strip.show()
        bequiet()
        
    icm20948.icm20948_Gyro_Accel_Read()
    icm20948.icm20948MagRead()
    icm20948.icm20948CalAvgValue()
    time.sleep(0.1)
    q0, q1, q2, q3 = icm20948.imuAHRSupdate(MotionVal[0] * 0.0175, MotionVal[1] * 0.0175,MotionVal[2] * 0.0175,
            MotionVal[3],MotionVal[4],MotionVal[5], 
            MotionVal[6], MotionVal[7], MotionVal[8])
    pitch = math.asin(-2 * q1 * q3 + 2 * q0 * q2)* 57.3
    roll  = math.atan2(2 * q2 * q3 + 2 * q0 * q1, -2 * q1 * q1 - 2 * q2* q2 + 1)* 57.3
    #yaw   = math.atan2(-2 * q1 * q2 - 2 * q0 * q3, 2 * q2 * q2 + 2 * q3 * q3 - 1) * 57.3
    
    print("-----")
    print('pitch' + str(pitch))
    print('roll', str(roll))
    print('Button' +str(button))


