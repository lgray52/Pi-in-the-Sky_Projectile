# type: ignore
# communicate over uart between boards
# code from https://learn.adafruit.com/uart-communication-between-two-circuitpython-boards/code

import busio
import board
from time import sleep
import digitalio
from projectileLib import getMessage

uart = busio.UART(board.GP0, board.GP1, baudrate=9600, timeout=0)

button = digitalio.DigitalInOut(board.GP15)
button.pull = digitalio.Pull.UP  # wire one leg to pin 15 ad the other to GROUND)

messageStarted = False  # wait for a message to start
alreadyPressed = False  # wait for button to be pressed

while True:
    if button.value == False:  # if its been 3 seconds or more since a message last sent, send a message
        if alreadyPressed == False:
            uart.write(bytes(f"<Start>", "ascii"))
            print(f"Starting data collection ...")
            sleep(1)
            alreadyPressed = True
        
        elif alreadyPressed == True:
            uart.write(bytes(f"<Stop>", "ascii"))
            print(f"Stopping data collection ...")
            sleep(1)
            alreadyPressed = False

    message = getMessage(uart)

    if message == "Sending max height...":
        sleep(.1)
        maxHeight = getMessage(uart)
        print(f"Max height: {maxHeight}m")