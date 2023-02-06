# type: ignore

import adafruit_mpu6050 as imu
import busio
import board
from time import monotonic
from projectileLib import findMag

sdaPin = board.GP2  # define which SDA & SCL pins to use - HAVE TO BE CONNECTED TO SAME I2C ON PICO
sclPin = board.GP3
i2c = busio.I2C(sclPin, sdaPin)

mpu = imu.MPU6050(i2c)  # set up mpu sensor accelerometer

launched = False

while True:
    accel = findMag(mpu.acceleration)  # magnitude of acceleration

    if abs(accel) < 1 and launched == False:
        launchTime = monotonic()
        launched = True

    if abs(accel) < 1 and launched == True:
        stopTime = monotonic()
        totalTime = launchTime - stopTime
        print(totalTime)
        launched = False
