#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
import time
import pickle

from convert_image_2 import *
from serial_helper import *


width = 360
height = 720

imgparam = '--width 720 --height 360 -sh 100'

#width = 96
#height = 96

#3 for 24 bit mode, or 1 for 8 bit mode (worse resolution)
batch_height = 3
double_density = True

bitdensecode = -1
if batch_height == 1 and not double_density: bitdensecode = 0
elif batch_height == 1 and double_density: bitdensecode = 1
elif batch_height == 3 and not double_density: bitdensecode = 32
elif batch_height == 3 and double_density: bitdensecode = 33
else: print('Warning: unknown batch_height: possible values are 1 and 3 (8bit and 24bit mode)')

if True:
	#-ifx sketch / cartoon
	os.system('raspistill '+imgparam+' -t 2 -n -o /mnt/mmcblk0p2/own/img/camimg.jpg')
	imgbin = createBinaryImage('/mnt/mmcblk0p2/own/img/camimg.jpg',height,width)
	escpos = getESCPOSCode(imgbin.transpose(),width,height,batch_height)
	pickle.dump(escpos,open('escposimg.pkl','wb'))
else:
	escpos = pickle.load(open('escposimg.pkl','rb'))



for h in range(0,int(height/(batch_height*8))):
	send_serial(chr(27)+chr(42)+chr(bitdensecode)+chr(int(width%256))+chr(width//256))
	c = (h*batch_height*width);
	#print(escpos[c:c+batch_height*width])
	send_serial(escpos[c:c+batch_height*width].tobytes());
send_serial(chr(10))
send_serial(chr(27)+chr(82)+chr(2))
send_serial('Viele Gr'+chr(0x7d)+chr(0x7e)+'e!')
send_serial(chr(10))
send_serial("von Katha und Chris")
send_serial(chr(10))
from datetime import date
d = date.today()
send_serial(d.strftime('%d.%m im Jahre %Y'))
send_serial(chr(10)+chr(10)+chr(10))
