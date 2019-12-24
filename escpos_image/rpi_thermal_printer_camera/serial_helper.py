import serial
import time



def send_serial(send_bytes):
	ser = serial.Serial(port='/dev/ttyAMA0',baudrate=9600,timeout=9999,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
	#global ser
	if type(send_bytes) == bytes:
		ser.write(send_bytes)
	elif type(send_bytes) == str:
		ser.write(send_bytes.encode())
	elif type(send_bytes) == np.ndarray:
		ser.write(send_bytes.tobytes())

if __name__ == '__main__':
	send_serial("test string")
	send_serial(chr(10))
	
	
