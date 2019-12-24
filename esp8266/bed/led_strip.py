import machine, neopixel
import time

import urandom

# helper

def randint(min,max):
	if min == max:
		return min
	return urandom.getrandbits(32) % (max-min) + min

def get_current_time():
	return int(round(time.time() * 1000))

def reload_module(module):
	import sys
	del sys.modules[module]
	__import__(module)


def rand_color(bpp,max_intensity):
	return [randint(0,max_intensity[i]) for i in range(bpp)]


def get_np(pin,n,bpp):
	np = neopixel.NeoPixel(pin=machine.Pin(pin), n=n, bpp=bpp)
	np.dim = 1
	np.h = 1
	np.w = n
	np.color_order=[1,0,2]
	return np

def get_np_small():
	n = 30 # number of pixels
	bpp = 3 # number of color dimensions
	led_strip_pin = 4
	np = neopixel.NeoPixel(pin=machine.Pin(led_strip_pin), n=n, bpp=bpp)

	np.dim = 2
	np.h = 3
	np.w = 10
	np.color_order=[1,0,2]
	np.zigzack_top=True
	np.zigzack_left=True
	return np


def get_np_pixelmatrix():
	n = 300 # number of pixels
	bpp = 4 # number of color dimensions
	led_strip_pin = 4
	np = neopixel.NeoPixel(pin=machine.Pin(led_strip_pin), n=n, bpp=bpp)

	np.dim = 2
	np.h = 10
	np.w = 30
	np.color_order=[1,0,2,3]
	np.zigzack_top=True
	np.zigzack_left=True
	return np

# img = [[[0] * d for j in range(w)] for i in range(h)]

def draw_pixel_2d(np, pixel, color):
	i,j = pixel
	for k in range(np.bpp):
		if i % 2 == 0:
			np.buf[(i*np.w*4) + j*4 + np.color_order[k]] = color[k]
		else: 
			np.buf[(i*np.w*4) + (np.w-j-1)*4 + np.color_order[k]] = color[k]


def draw_rect(np, p1, p2, col):
	y1,y2 = min(p1[0],p2[0]),max(p1[0],p2[0])
	x1,x2 = min(p1[1],p2[1]),max(p1[1],p2[1])
	for i in range(y1,y2+1):
		for j in range(x1,x2+1):
			draw_pixel_2d(np,[i,j],col)


def draw_gfx(np,gfx,pos,col):
	for gfx_i,img_i in enumerate(range(pos[0],pos[0]+len(gfx))):
		for gfx_j,img_j in enumerate(range(pos[1],pos[1]+len(gfx[0]))):
			if gfx[gfx_i][gfx_j] != '_':
				draw_pixel_2d(np,[img_i,img_j],col)


def draw_font(np,text,font,pos,col):
	width = len(font['a'].split()[0])
	for i, c in enumerate(text):
		if c in font.keys():
			gfx = font[c].split()
		else:
			gfx = font['*'].split()
		draw_gfx(np,gfx,[pos[0],pos[1]+i*(width+1)],col)

def running_text(np,text,font,pos_y=0,col=[50,0,0,0],increment=2,sleep_ms=20):
	text = text + ' >> '
	width = len(font['a'].split()[0])+1 #+1 space
	num_chars = int(np.w / width)
	index = 0
	while True:
		np.fill([0,0,0,0])
		draw_text = ''
		for i in range(num_chars):
			draw_text += text[(index+i)%len(text)]
		draw_font(np,draw_text,font,[pos_y,0],col)
		np.write()
		index += increment
		index = index % len(text)
		time.sleep_ms(sleep_ms)



def get_col_mix(col1,col2,step):
	rtn = []
	for i in range(len(col1)):
		rtn.append(col1[i] * (1-step) + col2[i] * step)
	return rtn

def int_vec(float_vec):
	rtn = []
	for i in float_vec:
		rtn.append(int(i))
	return rtn


class animation_base:
	def __init__(self,np):
		self.np = np
		self.running = False
		self._controls = None
	def init_controls(self,controls):
		'''example: an.init_controls([['int', 'delay',50,0,500],['int', 'brightness',50,0,255]])''' 
		self._controls = {}
		for c in controls:
			if c[0] == 'int' or c[0] == 'float':
				self._controls[c[1]] = {'val':c[2],'min':c[3],'max':c[4],'type':c[0]}
	def get_control(self,name):
		if name in self._controls:
			return self._controls[name]['val']
		else:
			raise ValueError('Field '+str(name)+' is not in animation controls')
	def set_control(self,name,new_value):
		if name in self._controls:
			if type(new_value) != type(self._controls[name]['val']):
				raise ValueError('Field '+str(name)+' has a different type than new value')
			if type(new_value) == int or type(new_value) == float:
				if new_value >= self._controls[name]['min'] and new_value <= self._controls[name]['max']:
					self._controls[name]['val'] = new_value
					return self._controls[name]['val']
				else: 
					raise ValueError('Field '+str(name)+' outside of specified range')
		else:
			raise ValueError('Field '+str(name)+' is not in animation controls')
	def step(self):
		pass
	def run(self):
		self.running = True
		while self.running:
			self.step() 

class animation_pulse(animation_base):
	def __init__(self,np):
		animation_base.__init__(self,np)
		self.increasing = False
		self.init_controls([['int', 'delay',10,0,5000],['int', 'brightness',20,0,255]])
		self.val = [self.get_control('brightness'),0,0]
	def step(self):
		self.val[0] += 1 if self.increasing else -1
		if self.val[0] <= 0:
			self.val[0] = 0
			self.increasing = True
		elif self.val[0] >= self.get_control('brightness'):
			self.val[0] = self.get_control('brightness')
			self.increasing = False
		if not self.np is None: 
			self.np.fill(self.val)
			self.np.write()
		else:
			print('setting color to: '+str(self.val))
		time.sleep_ms(self.get_control('delay'))
		

		

def animation_rand_col(np,max_brightness=255,time_step=2000,resolution=100):
	new_color = rand_color(np.bpp,[max_brightness,max_brightness,max_brightness])
	while True:
		old_color = new_color
		new_color = rand_color(np.bpp,[max_brightness,max_brightness,max_brightness])
		for i in range(resolution):
			print(new_color)
			np.fill(int_vec(get_col_mix(old_color,new_color,i/resolution)))
			np.write()
			time.sleep_ms(int(time_step/resolution))
		

def animation_rand_rect(np,max_brightness=20,time_sleep=500):
	while True:
		color = rand_color(np.bpp,[max_brightness,max_brightness,max_brightness,0])
		p1,p2 = [randint(0,np.h),randint(0,np.w)],[randint(0,np.h),randint(0,np.w)]
		draw_rect(np,p1,p2,color)
		np.write()
		print(color)
		time.sleep_ms(time_sleep)
		


import _thread

class thread:
	def __init__(self):
		self.stopped = False
		self.id = None
	def start(self, *args, **kwargs):
		self.stopped = False # if thread is restarted, resetting self.stopped to False
		self.id = _thread.start_new_thread(self.run, args, kwargs) #, [self] + [self.args], self.kwargs
	def run(self, *args, **kwargs):
		raise Exception('not implemented')
	def stop(self):
		self.stopped = True
		

class animation_rand_rects(thread):
	def __init__(self):
		thread.__init__(self)
	def run(self, np,max_brightness=20,time_sleep=500):
		while not self.stopped:
			color = rand_color(np.bpp,[max_brightness,max_brightness,max_brightness,0])
			p1,p2 = [randint(0,np.h),randint(0,np.w)],[randint(0,np.h),randint(0,np.w)]
			draw_rect(np,p1,p2,color)
			np.write()
			time.sleep_ms(time_sleep)

