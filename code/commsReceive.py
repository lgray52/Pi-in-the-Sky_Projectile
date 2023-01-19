# type: ignore
# communicate over uart between boards
# code from https://learn.adafruit.com/uart-communication-between-two-circuitpython-boards/code

import busio
import board
from ulab import numpy as np

uart = busio.UART(board.GP0, board.GP1, baudrate=9600, timeout=0)

from projectileLib import findMax, getMessage

np.ndarray.list = [4, 50, 3, 5, 7, 2, 1, 8, 3.2, 4.1, 2.3, 1.5, 1, 3, 4, 50, 5]

while True:
    message = getMessage(uart)
    
    if message == "Start":
        # Start data collection sequence
        print("Starting data collection ...")
    
    if message == "Stop":
        # Stop collecting data
        print("Ending data collection")
        max = findMax(list)
        print(max)
