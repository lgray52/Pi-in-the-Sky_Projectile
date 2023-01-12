# communicate over uart between boards
# code from https://learn.adafruit.com/uart-communication-between-two-circuitpython-boards/code


from projectileLib import getMessage

while True:
    messageNice = getMessage()
    
    if messageNice == "Start":
        # Start data collection sequence
        print("Starting data collection ...")
    
    if messageNice == "Stop":
        # Stop collecting data
        print("Ending data collection")