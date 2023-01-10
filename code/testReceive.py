# communicate over uart between boards
# code from https://learn.adafruit.com/uart-communication-between-two-circuitpython-boards/code

import adafruit_mpu6050 as imu
import busio
import board
import adafruit_mpl3115a2
from code.projectileLib import findMax, getMessage

sdaPin = board.GP2  # define which SDA & SCL pins to use - HAVE TO BE CONNECTED TO SAME I2C ON PICO
sclPin = board.GP3
i2c = busio.I2C(sclPin, sdaPin)

mpu = imu.MPU6050(i2c, address = 0x68)  # set up mpu sensor accelerometer - device address from test code

altimeter = adafruit_mpl3115a2.MPL3115A2(i2c, address = 0x60)  # set up altimeter

groundLevel = altimeter.altitude  # alimeter measures from sea level - set intial val of ground level

while True:
    message = getMessage()
    
    if message == "Start":
        # Start data collection sequence
        print("Starting data collection ...")
        altitudes = []

        while message == "Start":
            accelerationVals = mpu.acceleration
            angularVals = mpu.gyro

            alt = (altimeter.altitude - groundLevel)  # pull the current altitude above ground level
            altitudes.append(alt)

            message = getMessage()

            if message == "Stop":
                break
    
    if message == "Stop":
        # Stop collecting data
        print("Ending data collection")

        maxHeight = findMax(altitudes)