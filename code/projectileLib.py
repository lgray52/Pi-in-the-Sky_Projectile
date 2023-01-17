from ulab import numpy as np

def findMax(vals):
    meanVal = np.mean(vals)
    deviation = np.std(vals)

    for i in range(len(vals)):  # remove noise from data
        print(vals)
        zScore = (vals[i]-meanVal)/deviation

        if zScore > 3:  # remove outliers more than 3 standard deviations from mean
            vals.remove(vals[i])

    maxVal = max(vals)

    return maxVal

from time import sleep

def getMessage(uart):
    message = 0

    byte_read = uart.read(30)  # Read a bunch of bytes to make sure it gets the whole message
    sleep(.1)  # make sure it has enough tine to read the whole message while not causing awkward delay

    if not byte_read:
        # Nothing read.
        pass

    if byte_read:
        message = byte_read.decode()
        # print(message)
        print(f"Message received: {message}")
    
    return message