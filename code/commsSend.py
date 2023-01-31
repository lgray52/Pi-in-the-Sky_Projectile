# type: ignore
# communicate over uart between boards
# code from https://learn.adafruit.com/uart-communication-between-two-circuitpython-boards/code

'''uart setup'''
import busio
import board
uart = busio.UART(board.GP0, board.GP1, baudrate=9600, timeout=0)


'''button setup'''
import digitalio
button = digitalio.DigitalInOut(board.GP15)
button.pull = digitalio.Pull.UP  # wire one leg to pin 15 ad the other to GROUND)

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

'''general'''
from time import sleep
from projectileLib import getMessage

messageStarted = False  # wait for a message to start
alreadyPressed = False  # wait for button to be pressed

while True:
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

    message = getMessage(uart)

    if message == "Sending max height...":
        waitForMax = True

    if waitForMax:
        uart.write(bytes(f"Ready for max height", "ascii"))
        waitForMax = False


        # sleep(.1)
        # maxHeight = getMessage(uart)  # max height will send immediately after words - this is a little bit guess and check rn
        # maxStr = f"Max height: {maxHeight}m"  # set as var to pass to serial and the oled screen
        # print(maxStr)

        # # print to oled screen
        # maxLine = label.Label(FONT, text = maxStr, color = 0xFFFF00, x = 5, y = 5)  # format title line; set text to start at screen coordinate (5,5)
        # splash.append(maxLine)  # add maximum value to what the screen is showing

        # display.show(splash)  # print to screen