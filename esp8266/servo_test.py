from machine import Pin
import time
import Servo

def run(n):
	serv=Servo.Servo(Pin(n))

	#while wlan.isconnected():
	while 1:
		
		#open
		serv.write_angle(19)
		time.sleep_ms(2000) 
		
		#close
		serv.write_angle(160)
		time.sleep_ms(1000) 

		#ruttle
		for x in range(0, 9):
			serv.write_angle(80)
			time.sleep_ms(90) 
			serv.write_angle(170)
			time.sleep_ms(90) 
			
		
