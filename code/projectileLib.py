from statistics import mean, stdev

def findMax(vals):
    meanVal = mean(vals)
    deviation = stdev(vals)

    for i in vals:  # remove noise from data
        zScore = (vals[i]-meanVal)/deviation

        if zScore > 3:  # remove outliers more than 3 standard deviations from mean
            del vals[i]

    maxVal = max(vals)

    return maxVal


#Easy comms is a simple class that allows you to send and receive messages over a serial port.

from board import UART
from time import monotonic_ns

class Easy_comms:
 
    uart_id = 0
    baud_rate = 9600
    timeout = 1000 # milliseconds
    
    def __init__(self, uart_id:int, baud_rate:int=None):
        self.uart_id = uart_id
        if baud_rate: self.baud_rate = baud_rate

        # set the baud rate
        self.uart = UART(self.uart_id,self.baud_rate)

        # Initialise the UART serial port
        self.uart.init()
            
    def send(self, message:str):
        print(f'sending message: {message}')
        message = message + '\n'
        self.uart.write(bytes(message,'utf-8'))
        
    def start(self):
        message = "ahoy\n"
        print(message)
        self.send(message)

    def read(self)->str:
        start_time = monotonic_ns()
        current_time = start_time
        new_line = False
        message = ""
        while (not new_line) or (current_time <= (start_time + self.timeout)):
            if (self.uart.any() > 0):
                message = message + self.uart.read().decode('utf-8')
                if '\n' in message:
                    new_line = True
                    message = message.strip('\n')
                    # print(f'received message: {message}')
                    return message
        else:
            return None