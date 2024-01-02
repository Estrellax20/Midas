import network
import ubinascii
import urequests as requests
import time
from config import *
import machine
from lib.icm20948 import *
import socket
import random

icm20948=ICM20948()

while (True):
    
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
        #response = response.replace('AccZ', str(yaw))
