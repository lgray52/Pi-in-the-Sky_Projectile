# type: ignore

from ulab import numpy as np

def findMax(vals):
    real_vals = []
    medianVal = np.median(vals)
    # print("MEDIAN:", medianVal)
    devs = []

    for d in range(len(vals)):  # make a list of all the deviations from the median (mean ends up too skewed)
        devs.append(vals[d] - medianVal)
    
    deviation = np.sqrt((sum(devs))/len(vals))  # add them up and find the standard deviation
    # print("DEVIATION:", deviation)

    for i in reversed(range(len(vals))): # cycle backward through list so as not to mess up indices
        # print(vals)
        zScore = (vals[i]-medianVal)/deviation # find the z-score (how far removed from the data it is) based on median
        # print(vals[i])
        # print("z-score:", zScore)

        if zScore <= 3:  # # add all close enough vals to real vals list, excluding outliers > 3 stdevs from the median
            real_vals.append(vals[i])
            # print(real_vals)

    maxVal = max(real_vals)

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
        message = byte_read.decode()  # decode bytes into a string
        # print(message)
        print(f"Message received: {message}") 
    
    return message