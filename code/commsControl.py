# type: ignore
# communicate over uart between boards

'''uart setup'''
import busio
import board
uart = busio.UART(board.GP0, board.GP1, baudrate=9600, timeout=0)


'''arming button setup'''
import digitalio
button = digitalio.DigitalInOut(board.GP15)
button.pull = digitalio.Pull.UP  # wire one leg to pin 15 ad the other to GROUND 

'''oled screen setup'''
from adafruit_display_text import label
import adafruit_displayio_ssd1306
from terminalio import FONT
import displayio
displayio.release_displays()
sdaPin = board.GP2  # define which SDA & SCL pins to use - HAVE TO BE CONNECTED TO SAME I2C ON PICO
sclPin = board.GP3
i2c = busio.I2C(sclPin, sdaPin)
display_bus = displayio.I2CDisplay(i2c, device_address = 0x3d, reset = board.GP5)  # set up oled screen - device address from test code
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# set up OLED screen on a different i2c

'''general'''
from time import sleep
from projectileLib import getMessage

alreadyPressed = False  # wait for button to be pressed

while True:
    splash = displayio.Group()

    if button.value == False:  # if the button is pressed, send a message
        if alreadyPressed == False:  #
            uart.write(bytes(f"Start", "ascii"))
            print(f"Starting data collection ...")
            sleep(1)
            alreadyPressed = True
        
        elif alreadyPressed == True:
            uart.write(bytes(f"Stop", "ascii"))
            print(f"Stopping data collection ...")
            sleep(1)
            alreadyPressed = False

    if getMessage(uart) == "Sending data...":  # wait for message which tells sender to prepare to receieve max height
        waitForData = True
    else:
        waitForData = False

    if waitForData:  # tell receiever the sender is ready
        uart.write(bytes(f"Ready for max height", "ascii"))
        waitForData = False

        byte_read = uart.read(1)

        while byte_read == None:  # read one byte at a time until it gets a message which isn't None
            byte_read = uart.read(1)
            # print(byte_read)

        maxHeight = getMessage(uart)  # read the message after the first detected byte

        while maxHeight == 0:  # max height almost certainly should not be zero - correct transmission skip
            maxHeight = getMessage(uart)
            # print(maxHeight)

        maxStr = f"Max height: {maxHeight}m"  # set as var to pass to serial and the oled screen
        print(maxStr)

        # Time of flight
        uart.write(bytes(f"Ready for time", "ascii"))
        
        byte2_read = uart.read(1)

        while byte2_read == None:  # read one byte at a time until it gets a message which isn't None
            byte2_read = uart.read(1)
            # print(byte_read)
        
        tof = getMessage(uart)

        while tof == 0:  # same strategy as above
            tof = getMessage(uart)
            # print(tof)
        
        tofStr = f"Time: {tof}s"
        print(tofStr)

        # print to oled screen
        maxLine = label.Label(FONT, text = maxStr, color = 0xFFFF00, x = 5, y = 5)  # format title line; set text to start at screen coordinate (5,5)
        splash.append(maxLine)  # add maximum value to what the screen is showing

        tofLine = label.Label(FONT, text = tofStr, color = 0xFFFF00, x = 5, y = 15)
        splash.append(tofLine)  # add maximum value to what the screen is showing

        display.show(splash)  # print to screen