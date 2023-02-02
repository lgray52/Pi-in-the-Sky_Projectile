# type: ignore
# communicate over uart between boards
# code from https://learn.adafruit.com/uart-communication-between-two-circuitpython-boards/code

import busio
import board
from ulab import numpy as np
import adafruit_mpl3115a2
from time import sleep

uart = busio.UART(board.GP0, board.GP1, baudrate=9600, timeout=0)

from projectileLib import findMax, getMessage

# need to use a numpy array to use median
# list = np.array([4, 50, 3, 5, 7, 2, 1, 8, 3.2, 4.1, 2.3, 1.5, 1, 3, 4, 50, 5, 35, 100, 200, 1])

sdaPin = board.GP2  # define which SDA & SCL pins to use - HAVE TO BE CONNECTED TO SAME I2C ON PICO
sclPin = board.GP3
i2c = busio.I2C(sclPin, sdaPin)

altimeter = adafruit_mpl3115a2.MPL3115A2(i2c, address = 0x60)  # set up altimeter
groundLevel = altimeter.altitude  # alimeter measures from sea level - set intial val of ground level

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

        sleep(.1)
        uart.write(bytes(f"Sending max height...", "ascii"))
        message = getMessage(uart)

        while message == 0:
            message = getMessage(uart)

        if message == "Ready for max height":
            uart.write(bytes(f"{str(max)}", "ascii"))