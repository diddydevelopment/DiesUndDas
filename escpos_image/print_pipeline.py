#!/usr/bin/env python


import os
import sys
import time
import pickle

from convert_image_2 import *
from serial_helper import *


width = 360
height = 280

if True:
	os.system('raspistill --width 800 --height 360 -t 1 -o /home/pi/src/DiesUndDas/escpos_image/camimg.jpg')
	imgbin = createBinaryImage('camimg.jpg',height,width)
	escpos = getESCPOSCode(imgbin.transpose(),width,height)
	pickle.dump(escpos,open('escposimg.pkl','wb'))
else:
	escpos = pickle.load(open('escposimg.pkl','rb'))

batch_height = 1
for h in range(0,height/(batch_height*8)):
	send_serial(chr(27)+chr(42)+chr(1)+chr(int(width%256))+chr(width//256))
	c = (h*batch_height*width);
	send_serial(escpos[c:c+batch_height*width]);

send_serial(chr(10)+chr(10)+chr(10))
