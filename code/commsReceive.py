# type: ignore
# communicate over uart between boards
# code from https://learn.adafruit.com/uart-communication-between-two-circuitpython-boards/code

import busio
import board

uart = busio.UART(board.GP0, board.GP1, baudrate=9600, timeout=0)

from projectileLib import getMessage

while True:
    message = getMessage(uart)
    
    if message == "Start":
        # Start data collection sequence
        print("Starting data collection ...")
    
    if message == "Stop":
        # Stop collecting data
        print("Ending data collection")