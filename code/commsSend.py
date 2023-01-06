# communicate over uart between boards
# code from https://learn.adafruit.com/uart-communication-between-two-circuitpython-boards/code

import busio
import board
from time import sleep
import digitalio

uart = busio.UART(board.GP0, board.GP1, baudrate=9600, timeout=0)

button = digitalio.DigitalInOut(board.GP15)
button.pull = digitalio.Pull.UP  # wire one leg to pin 15 ad the other to GROUND)

messageStarted = False  # wait for a message to start
alreadyPressed = False

while True:
    if button.value == False:  # if its been 3 seconds or more since a message last sent, send a message
        if alreadyPressed == False:
            uart.write(bytes(f"<Start>", "ascii"))
            print(f"Starting data collection ...")
            sleep(1)
            alreadyPressed = True
        
        if alreadyPressed == True:
            uart.write(bytes(f"<Stop>", "ascii"))
            print(f"Stopping data collection ...")
            sleep(1)
            alreadyPressed = False
    

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