# communicate over uart between boards

import busio
import board
from time import monotonic, sleep

uart = busio.UART(board.TX, board.RX, baudrate=9600, timeout=0)

interval = 3.0  # send a message every 2 seconds
timeLastSent = 0  # variable to store the last time a message was sent

messageStarted = False  # wait for a message to start

while True:
    now = monotonic()

    if now - timeLastSent >= interval:  # if its been 3 seconds or more since a message last sent, send a message
        uart.write(bytes(f"<check>"))
        print(f"Sending message ...")
        timeLastSent = now  # set last message sent time to current time
    

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
            # Now we have a complete message. Convert it to a string
            print(f"Message received: {message}")
            messageStarted = False
    
    else:
        # Accumulate message byte.
        message.append(chr(byte_read[0]))