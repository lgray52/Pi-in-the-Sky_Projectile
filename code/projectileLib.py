# from statistics import mean, stdev

# def findMax(vals):
#     meanVal = mean(vals)
#     deviation = stdev(vals)

#     for i in vals:  # remove noise from data
#         zScore = (vals[i]-meanVal)/deviation

#         if zScore > 3:  # remove outliers more than 3 standard deviations from mean
#             del vals[i]

#     maxVal = max(vals)

#     return maxVal

def getMessage(uart):
    messageStarted = False  # wait for a message to start
    messageNice = 0

    byte_read = uart.read(1)  # Read one byte over UART lines

    if not byte_read:
        # Nothing read.
        pass

    if byte_read == b"<":
        # Start of message. Start accumulating bytes, but don't record the "<".
        message = []
        messageStarted = True
        pass

    if messageStarted == True:
        if byte_read == b">":
            # End of message. Don't record the ">".
            # Now we have a complete message. Convert it to a string.
            messageNice = "".join(message)  # join letters together into a nicer format
            print(f"Message received: {messageNice}")
            messageStarted = False
    
        else:
            # Accumulate message byte by byte - this strings the message together.
            message.append(chr(byte_read[0]))
    
    return messageNice