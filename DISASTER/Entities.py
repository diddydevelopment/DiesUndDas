import numpy as np
import random as rn

import pyglet
from pyglet.window import key

from time import time

from Dir import Dir
from DisplayObject import *
from globals import *

class Entity(DisplayObject):
	def __init__(self,pos,imgpos,speed):
		super(Entity,self).__init__(pos,imgpos)
		self.speed = speed
	def update(self):
		raise NotImplementedError('Please implement update method')


class Rock(Entity):
	MAX_SPEED = 5
	def __init__(self,pos=None,speed=None):
		self.dir = rn.randint(0,3)
		if pos is None:
			if self.dir == Dir.down:
				pos = np.array([rn.random() * WINDOW_SIZE[0], WINDOW_SIZE[1]])
				self.curSpeed = [0, -rn.random() * Rock.MAX_SPEED]
			elif self.dir == Dir.up:
				pos = np.array([rn.random() * WINDOW_SIZE[0], -SPRITE_SIZE])
				self.curSpeed = [0, rn.random() * Rock.MAX_SPEED]
			elif self.dir == Dir.right:
				pos = np.array([-SPRITE_SIZE, rn.random() * WINDOW_SIZE[1]])
				self.curSpeed = [rn.random() * Rock.MAX_SPEED,0]
			elif self.dir == Dir.left:
				pos = np.array([WINDOW_SIZE[0], rn.random() * WINDOW_SIZE[1]])
				self.curSpeed = [-rn.random() * Rock.MAX_SPEED,0]
		super(Rock, self).__init__(pos, [50,0,25,25],Rock.MAX_SPEED)

	def update(self,dt):
		self.move(self.curSpeed)
		if self.dir == Dir.down and self.pos[1] < -SPRITE_SIZE:
			self.pos[1] = WINDOW_SIZE[1]
		elif self.dir == Dir.up and self.pos[1] > WINDOW_SIZE[1]:
			self.pos[1] = -SPRITE_SIZE
		elif self.dir == Dir.right and self.pos[0] > WINDOW_SIZE[0]:
			self.pos[0] = -SPRITE_SIZE
		elif self.dir == Dir.left and self.pos[0] < SPRITE_SIZE:
			self.pos[0] = WINDOW_SIZE[0]


class Ship(Entity):
	SHOTTIME = .1
	TRACTION = .1
	
	def __init__(self,pos,imgpos,speed):
		super(Ship,self).__init__(pos,imgpos,speed)
		self.dir = Dir.up
		self.dx = 0
		self.dy = 0
		self.lastShot = time()
		self.shoot = False
		self.rotate = True
	 
	def setShooting(self,s):
		self.shoot = s
	 
	def updateDirection(self):
		if self.dx < 0 and self.dy > 0:
			self.dir= Dir.upleft
		elif self.dx > 0 and self.dy > 0:
			self.dir= Dir.upright
		elif self.dx < 0 and self.dy < 0:
			self.dir= Dir.downleft
		elif self.dx > 0 and self.dy < 0:
			self.dir= Dir.downright
		elif self.dy > 0:
			self.dir= Dir.up
		elif self.dy < 0:
			self.dir= Dir.down
		elif self.dx < 0 :
			self.dir= Dir.left
		elif self.dx > 0:
			self.dir= Dir.right
			
	 
	def updateRotationImg(self):
		if self.dir == Dir.left:
			self.sprite.rotation = 270
		elif self.dir == Dir.right:
			self.sprite.rotation = 90
		elif self.dir == Dir.up:
			self.sprite.rotation = 0
		elif self.dir == Dir.down:
			self.sprite.rotation = 180
		elif self.dir == Dir.upright:
			self.sprite.rotation = 45
		elif self.dir == Dir.downright:
			self.sprite.rotation = 135
		elif self.dir == Dir.downleft:
			self.sprite.rotation = 225
		elif self.dir == Dir.upleft:
			self.sprite.rotation = 315
	
		
	def setSpeed(self,vx,vy):
		self.dx = self.speed[0]*vx
		self.dy = self.speed[1]*vy
	   

	def update(self,dt):
		self.dx *=Ship.TRACTION
		self.dy *=Ship.TRACTION
		
		if(abs(self.dx)<0.001):
			self.dx=0
		if(abs(self.dy)<0.001):
			self.dy=0
		
		self.updateDirection()
		
		if self.rotate:
			self.updateRotationImg()
		
		self.move(np.array([int(self.dx),int(self.dy)]))
		

		
		
		
		
