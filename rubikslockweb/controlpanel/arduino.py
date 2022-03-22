# import serial
# import time

# ser = serial.Serial('COM7', 9800, timeout=1)

# def lock():
#     time.sleep(0.5)
#     ser.write(b'H')   # send the pyte string 'H'
#     # ser.close()

# def unlock():
#     time.sleep(0.5)   # wait 0.5 seconds
#     ser.write(b'L')   # send the byte string 'L'
#     # ser.close()

# lock()
# unlock()

import pyfirmata
import time

board = pyfirmata.Arduino('COM7')

# while True:
#     board.digital[6].write(1)
#     time.sleep(1)
#     board.digital[6].write(0)
#     time.sleep(1)

def lock():
    board.digital[6].write(1)
    time.sleep(1)

def unlock():
    board.digital[6].write(0)
    time.sleep(1)