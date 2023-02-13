# type: ignore
# communicate over uart between boards
# code from https://learn.adafruit.com/uart-communication-between-two-circuitpython-boards/code

import busio
import board
from ulab import numpy as np
from time import sleep, monotonic

uart = busio.UART(board.GP0, board.GP1, baudrate=9600, timeout=0)

from projectileLib import findMax, getMessage, findMag

sdaPin = board.GP2  # define which SDA & SCL pins to use - HAVE TO BE CONNECTED TO SAME I2C ON PICO
sclPin = board.GP3
i2c = busio.I2C(sclPin, sdaPin)

"""altimeter"""
import adafruit_mpl3115a2

altimeter = adafruit_mpl3115a2.MPL3115A2(i2c, address = 0x60)  # set up altimeter
groundLevel = altimeter.altitude  # alimeter measures from sea level - set intial val of ground level

"""accelerometer"""
import adafruit_mpu6050 as imu

mpu = imu.MPU6050(i2c)  # set up mpu sensor accelerometer
launched = False

while True:
    message = getMessage(uart)
    # print(message)
    
    if message == "Start":
        alts = []
        # Start data collection sequence
        print("Starting data collection ...")

        while message == "Start" or message == 0: 
            message = getMessage(uart)  # check constantly for message?
            # print(message)
            alt = altimeter.altitude  # pull the current altitude
            abvG = alt - groundLevel  # above ground height is the difference between altitude and ground level
            alts.append(abvG)  # accumulate a list of all the altitudes recorded by the altimeter

    
    if message == "Stop":
        # Stop collecting data
        print("Ending data collection")
        print(alts)
        altsFinal = np.array(alts)  # make altitudes into a numpy array so it can be used
        max = findMax(altsFinal)  # take maxmimum value and print
        print(f"Max height: {max}")


        """send max height to control box"""
        uart.write(bytes(f"Sending max height...", "ascii"))  # send sender a message to prepare to receive max height
        message = getMessage(uart)

        while message == 0:  # wait until message is sent back over that sender is ready to receive
            message = getMessage(uart)  # continue to check message

        if message == "Ready for max height":  # when confirmation is received, send max height
            uart.write(bytes(f" {str(max)}", "ascii"))  # need to add one space before message so that it can read that a byte is sent before getting the whole message
        

        """send time of flight to control box"""
        uart.write(bytes(f"Sending time of flight...", "ascii"))
        message = getMessage(uart)

        while message == 0:
            message = getMessage(uart)
        
        if message == "Ready for time":
            uart.write(bytes(f" {str(totalTime)}", "ascii"))

    accel = findMag(mpu.acceleration)  # magnitude of acceleration
    times = []

    if abs(accel) < 1 and launched == False:  # when projectile enters freefall
        launchTime = monotonic()  # record the time it launched
        print(launchTime)
        launched = True

    if abs(accel) > 11 and launched == True:  # when it experiences an acceleration from hitting the ground
        stopTime = monotonic()  # record the time it hit the ground
        print(accel)
        totalTime =  stopTime - launchTime  # find time between start and stop - tof
        times.append(totalTime)

        if len(times) > 1:  # in case mutiple values are found take the longest time - should avoid bounce activations
            totalTime = max(times)
        
        print(f"Total time of flight: {totalTime}")

        launched = False