import network
import ubinascii
import socket
import random
import urequests as requests
import time

from adc import *
from config import *
from i2cc import *
from lib.buzzer import *
from lib.icm20948 import *
from lib.neopixel import Neopixel

I2C_SDA_PIN = 0
I2C_SCL_PIN = 1
ADR = 0x5A
MEM1 = 0x01
BUF1 = 0x00
i2c=I2C(0,sda=Pin(I2C_SDA_PIN), scl=Pin(I2C_SCL_PIN), freq=400000)

print('Start!')

# Initialize the ICM20948 sensor object
icm20948 = ICM20948()

# Initialize the Neopixel object to control RGB LED lights
strip = Neopixel(1, 0, LED_PIN, "GRB")

# Set the brightness of the LED lights to the value defined as LED_BRIGHTNESS
strip.brightness(LED_BRIGHTNESS)

# Variable to control the vibration motor
vibration_enabled = 0

# ADC pin
adc_pin = machine.ADC(machine.Pin(26))

# Main program loop
while True:
    # Show the current state of the LED lights on the Neopixel strip
    strip.show()

    # Read Gyroscope and Accelerometer data from the ICM20948 sensor
    icm20948.icm20948_Gyro_Accel_Read()

    # Read Magnetometer data from the ICM20948 sensor
    icm20948.icm20948MagRead()

    # Calculate the average calibration values for the ICM20948 sensor
    icm20948.icm20948CalAvgValue()

    # Pause for 0.1 seconds
    time.sleep(0.01)

    # Update the AHRS (Attitude and Heading Reference System) values using sensor data
    q0, q1, q2, q3 = icm20948.imuAHRSupdate(
        MotionVal[0] * 0.0175, MotionVal[1] * 0.0175, MotionVal[2] * 0.0175,
        MotionVal[3], MotionVal[4], MotionVal[5],
        MotionVal[6], MotionVal[7], MotionVal[8]
    )

    # Calculate pitch and roll angles from quaternion values
    pitch = math.asin(-2 * q1 * q3 + 2 * q0 * q2) * 57.3
    roll = math.atan2(2 * q2 * q3 + 2 * q0 * q1, -2 * q1 * q1 - 2 * q2 * q2 + 1) * 57.3
    
    # Read ADC value
    scaled_adc_value = adc_scaled()

    # Toggle vibration motor variable when ADC value reaches 1000
    if scaled_adc_value >= 3000 and not vibration_enabled:
        vibration_enabled = 1
        strip.fill(LED_COLORS['blue'])
        strip.show()
        vibration()
        
        print("Vibration Enabled:", vibration_enabled)

    elif scaled_adc_value < 3000 and vibration_enabled:
        vibration_enabled = 0
        
        # Change the LED color to red
        strip.fill(LED_COLORS['yellow'])
        strip.show()
        
        print("Vibration Disabled:", vibration_enabled)

        # Print pitch and roll values in a formatted table
        print("-----")
        print('{:<10} {:<10}'.format('Pitch', 'Roll'))
        print('{:<10.2f} {:<10.2f}'.format(pitch, roll))

        # Print adc value
        print("Scaled_ADC_Value:", scaled_adc_value)
