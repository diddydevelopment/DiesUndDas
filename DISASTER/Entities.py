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
		
	def randomStartPos(self):
		self.dir = rn.randint(0,3)
		if self.dir == Dir.down:
			self.pos = np.array([rn.random() * WINDOW_SIZE[0], WINDOW_SIZE[1]])
		elif self.dir == Dir.up:
			self.pos = np.array([rn.random() * WINDOW_SIZE[0], -SPRITE_SIZE])
		elif self.dir == Dir.right:
			self.pos = np.array([-SPRITE_SIZE, rn.random() * WINDOW_SIZE[1]])
		elif self.dir == Dir.left:
			self.pos = np.array([WINDOW_SIZE[0], rn.random() * WINDOW_SIZE[1]])
				
class Rock(Entity):
	MAX_SPEED = 5
	def __init__(self,pos=None,speed=None):
		self.randomStartPos()
		
		if self.dir == Dir.down:
			self.curSpeed = [0, -rn.random() * Rock.MAX_SPEED]
		elif self.dir == Dir.up:
			self.curSpeed = [0, rn.random() * Rock.MAX_SPEED]
		elif self.dir == Dir.right:
			self.curSpeed = [rn.random() * Rock.MAX_SPEED,0]
		elif self.dir == Dir.left:
			self.curSpeed = [-rn.random() * Rock.MAX_SPEED,0]
				
		super(Rock, self).__init__(self.pos, [50,0,25,25],Rock.MAX_SPEED)

	def update(self,dt):
		self.move(self.curSpeed)
		
		'''
		if self.dir == Dir.down and self.pos[1] < -SPRITE_SIZE:
			self.pos[1] = WINDOW_SIZE[1]
		elif self.dir == Dir.up and self.pos[1] > WINDOW_SIZE[1]:
			self.pos[1] = -SPRITE_SIZE
		elif self.dir == Dir.right and self.pos[0] > WINDOW_SIZE[0]:
			self.pos[0] = -SPRITE_SIZE
		elif self.dir == Dir.left and self.pos[0] < SPRITE_SIZE:
			self.pos[0] = WINDOW_SIZE[0]
		'''

class Ship(Entity):
	TRACTION = .2
	
	def __init__(self,pos,imgpos,speed):
		super(Ship,self).__init__(pos,imgpos,speed)
		self.dir = Dir.up
		self.dx = 0
		self.dy = 0
		self.lastShot = time()
		self.shotTime = .1
		self.shoot = False
		self.rotate = True
		self.bulletType=np.array([25,0,4,4])
	 
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
		self.dx = self.speed*vx
		self.dy = self.speed*vy
	   
	   
	def checkShooting(self):
		if self.shoot and self.lastShot+self.shotTime < time():
			l=LaserBeam(self.pos.copy(),self.dir,self.bulletType)
			self.addBullet(l)
			self.lastShot = time()
			#laserSound.play()

	def update(self,dt):
		
		print(self.dx)
		print(self.dy)
		
		self.dx *=Ship.TRACTION
		self.dy *=Ship.TRACTION
		
		if(abs(self.dx)<0.01):
			self.dx=0
		if(abs(self.dy)<0.01):
			self.dy=0
		
		self.updateDirection()
		
		if self.rotate:
			self.updateRotationImg()
		
		self.move(np.array([self.dx,self.dy]))
		
		self.checkShooting()
		
		
		
		
