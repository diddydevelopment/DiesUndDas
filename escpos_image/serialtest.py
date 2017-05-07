import serial
import time
ser = serial.Serial(port='/dev/usbdev7.3',baudrate=9600,timeout=1,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)

#ser.write("hello world")
ser.write([10])
