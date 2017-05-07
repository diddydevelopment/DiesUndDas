#!/usr/bin/env python
"""Basic blinking led example.

The led on A20-OLinuXino-MICRO  blinks with rate of 1Hz like "heartbeat".
"""

import os
import sys
import time

if not os.getegid() == 0:
    sys.exit('Script must be run as root')


import time
from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector

tx = port.PA11
rx = port.PA12

baud = 0.92/9600.0

def mySleep(sec):
	curtime = time.time()
	while(time.time()<=curtime+sec):
		pass


def sendTx(sendCharASCII):
	sendByte = '{0:b}'.format(sendCharASCII).zfill(8)
	sendByte = sendByte[::-1]
	print(sendByte)
	sendByteInt = [gpio.HIGH if bit=='1' else gpio.LOW for bit in sendByte]
	gpio.output(tx,gpio.LOW)
	mySleep(baud)
	for bit in sendByteInt:
		#print('sending '+bit)
		gpio.output(tx,bit)
		mySleep(baud)
	gpio.output(tx,gpio.HIGH)
	mySleep(baud*10)


gpio.init()
gpio.setcfg(tx, gpio.OUTPUT)
gpio.setcfg(rx, gpio.INPUT)

gpio.output(tx,1)
gpio.output(rx,1)
mySleep(1)

if(True):
	from convert_image_2 import *
	width = 248
	height = 128
	imgbin = createBinaryImage('portrait.jpg',width,height)

	escpos = getESCPOSCode(imgbin,width,height)

	print(escpos)
	batch_height = 1


	for h in range(0,height/(batch_height*8)):
	#for h in range(0,1):
		sendTx(27);
		sendTx(42);
		sendTx(1);
		sendTx(int(width));
		sendTx(0);
		for w in range(0,batch_height*width):
		  c = (h*batch_height*width);
		  sendTx(escpos[c+w]);

	#plt.imshow(imgbin,cmap='Greys',  interpolation='nearest')
	#plt.show()
else:
	sendString = 'Halli Hallo hier kommt ein ziemlich langer string'
	for c in sendString:
		sendTx(ord(c))

	sendTx(10)
	sendTx(10)
	sendTx(10)
