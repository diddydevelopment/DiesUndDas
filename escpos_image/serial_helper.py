import serial
import time
ser = serial.Serial(port='/dev/ttyAMA0',baudrate=9600,timeout=1,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)

def send_serial(send_bytes):
	ser.write(send_bytes)

if __name__ == '__main__':
	send_serial("test string")
	send_serial(chr(10))
	
	
