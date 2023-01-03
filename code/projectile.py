# type: ignore

import adafruit_mpu6050 as imu
import busio
import board
import adafruit_mpl3115a2
from code.projectileLib import findMax

sdaPin = board.GP2  # define which SDA & SCL pins to use - HAVE TO BE CONNECTED TO SAME I2C ON PICO
sclPin = board.GP3
i2c = busio.I2C(sclPin, sdaPin)

mpu = imu.MPU6050(i2c, address = 0x68)  # set up mpu sensor accelerometer - device address from test code

altimeter = adafruit_mpl3115a2.MPL3115A2(i2c, address = 0x60)  # set up altimeter

groundLevel = altimeter.altitude  # alimeter measures from sea level - set intial val of ground level

altitudes = []

while # something:
    accelerationVals = mpu.acceleration
    angularVals = mpu.gyro
    alt = (altimeter.altitude - groundLevel)  # pull the current altitude above ground level


altitudes.append(alt)