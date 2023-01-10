# communicate over uart between boards
# code from https://learn.adafruit.com/uart-communication-between-two-circuitpython-boards/code

import busio
import board
from time import monotonic, sleep

uart = busio.UART(board.GP0, board.GP1, baudrate=9600, timeout=0)

interval = 3.0  # send a message every 2 seconds
timeLastSent = 0  # variable to store the last time a message was sent

messageStarted = False  # wait for a message to start

while True:
    now = monotonic()  # set current time

    if now - timeLastSent >= interval:  # if its been 3 seconds or more since a message last sent, send a message
        uart.write(bytes(f"<check>", "ascii"))  # needs the "ascii" to work, bytes() needs two arguments
        print(f"Sending message ...")
        timeLastSent = now  # set last message sent time to current time
    

    byte_read = uart.read(1)  # Read one byte over UART lines

    if not byte_read:
        # Nothing read.
        continue

    if byte_read == b"<":
        # Start of message. Start accumulating bytes, but don't record the "<".
        message = []
        messageStarted = True  # its true that the message has started - initate next loop
        continue

    if messageStarted:
        if byte_read == b">":
            # End of message. Don't record the ">".
            # Now we have a complete message. Convert it to a string.
            messageNice = "".join(message)  # join letters together into a nicer format
            print(f"Message received: {messageNice}")
            messageStarted = False  # finish the message
    
        else:
            # Accumulate message byte by byte - this strings the message together.
            message.append(chr(byte_read[0]))
