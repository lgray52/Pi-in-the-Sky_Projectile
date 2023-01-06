# communicate over uart between boards
# code from https://learn.adafruit.com/uart-communication-between-two-circuitpython-boards/code

import busio
import board
from time import sleep

uart = busio.UART(board.GP0, board.GP1, baudrate=9600, timeout=0)

messageStarted = False  # wait for a message to start

while True:
    byte_read = uart.read(1)  # Read one byte over UART lines

    if not byte_read:
        # Nothing read.
        continue

    if byte_read == b"<":
        # Start of message. Start accumulating bytes, but don't record the "<".
        message = []
        messageStarted = True
        continue

    if messageStarted:
        if byte_read == b">":
            # End of message. Don't record the ">".
            # Now we have a complete message. Convert it to a string.
            messageNice = "".join(message)  # join letters together into a nicer format
            print(f"Message received: {messageNice}")
            messageStarted = False
    
        else:
            # Accumulate message byte by byte - this strings the message together.
            message.append(chr(byte_read[0]))
    
    if messageNice == "Start":
        # Start data collection sequence
        print("Starting data collection ...")

    if messageNice == "Stop":
        # Stop collecting data
        print("Ending data collection")