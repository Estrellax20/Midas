import network
import ubinascii
from lib.buzzer import *
import urequests as requests
import time
from config import *
import machine
from lib.icm20948 import *
import socket
import random
from lib.neopixel import Neopixel
#from i2c import *

print('Start!')

# Initialization of the vibration motor
#setup_haptic_motor()

# Initialize the ICM20948 sensor object
icm20948 = ICM20948()

# Initialize the Neopixel object to control RGB LED lights
strip = Neopixel(1, 0, LED_PIN, "GRB")

# Set the brightness of the LED lights to the value defined as LED_BRIGHTNESS
strip.brightness(LED_BRIGHTNESS)

# Fill all the LED lights on the Neopixel strip with the color yellow
strip.fill(LED_COLORS['yellow'])

# Variable to control the vibration motor
vibration_enabled = 0

# ADC pin
adc_pin = machine.ADC(Pin(26))

# Main program loop
while (True):    
    # Show the current state of the LED lights on the Neopixel strip
    strip.show()
    
    # Read Gyroscope and Accelerometer data from the ICM20948 sensor
    icm20948.icm20948_Gyro_Accel_Read()

    # Read Magnetometer data from the ICM20948 sensor
    icm20948.icm20948MagRead()

    # Calculate the average calibration values for the ICM20948 sensor
    icm20948.icm20948CalAvgValue()

    # Pause for 0.1 seconds
    time.sleep(0.1)

    # Update the AHRS (Attitude and Heading Reference System) values using sensor data
    q0, q1, q2, q3 = icm20948.imuAHRSupdate(
        MotionVal[0] * 0.0175, MotionVal[1] * 0.0175, MotionVal[2] * 0.0175,
        MotionVal[3], MotionVal[4], MotionVal[5],
        MotionVal[6], MotionVal[7], MotionVal[8]
    )

    # Calculate pitch and roll angles from quaternion values
    pitch = math.asin(-2 * q1 * q3 + 2 * q0 * q2) * 57.3
    roll = math.atan2(2 * q2 * q3 + 2 * q0 * q1, -2 * q1 * q1 - 2 * q2 * q2 + 1) * 57.3

    # Print pitch and roll values in a formatted table
    print("-----")
    print('{:<10} {:<10}'.format('Pitch', 'Roll'))
    print('{:<10.2f} {:<10.2f}'.format(pitch, roll))
    
    # Read ADC value
    adc_value = adc_pin.read_u16()

    # Toggle vibration motor variable when ADC value reaches 1000
    if adc_value >= 1000:
        vibration_enabled = 1 - vibration_enabled
        print("Vibration Enabled:", vibration_enabled)

    # Activate/deactivate vibration motor based on the variable
#    if vibration_enabled:
#       vibrate_haptic_motor()
    