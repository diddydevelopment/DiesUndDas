import numpy as np
import random as rn

import pyglet
from pyglet.window import key

from time import time

from Dir import Dir
from DisplayObject import *
from Entities import *
from globals import *


class Enemy(Ship):
	PLAYER=None
	
	def __init__(self,pos,imgpos,speed):
		super(Enemy,self).__init__(pos,imgpos,speed)


	def getDirToPlayer(self):
		diffX=Enemy.PLAYER.pos[0]-self.pos[0]
		diffY=Enemy.PLAYER.pos[1]-self.pos[1]
		
		dirToPlayer= Dir.up
		
		if diffX < 0 and diffY > 0:
			dirToPlayer= Dir.upleft
		elif diffX  > 0 and diffY > 0:
			dirToPlayer= Dir.upright
		elif diffX  < 0 and diffY < 0:
			dirToPlayer= Dir.downleft
		elif diffX  > 0 and diffY< 0:
			dirToPlayer= Dir.downright
		elif diffY > 0:
			dirToPlayer= Dir.up
		elif diffY < 0:
			dirToPlayer= Dir.down
		elif diffX  < 0 :
			dirToPlayer= Dir.left
		elif diffX  > 0:
			dirToPlayer= Dir.right
			
		return dirToPlayer

	def checkShooting(self):
		if self.shoot and self.lastShot+self.shotTime < time():
			dirToPlayer=self.getDirToPlayer()
			l=LaserBeam(self.pos.copy(),dirToPlayer,self.bulletType)
			l.targetType='Player'
			self.addBullet(l)
			self.lastShot = time()
			#laserSound.play()


class Mothership(Enemy):
	def __init__(self,pos,imgpos,speed):
		super(Mothership,self).__init__(pos,imgpos,speed)
		self.targetPos = np.array(pos,np.float32)
		self.bulletType=np.array([33,0,4,4])
		self.shotTime = .1
		
	def update(self,dt):
		
		diffX=self.pos[0]-self.targetPos[0]
		diffY=self.pos[1]-self.targetPos[1]
		
		
		if(abs(diffX)<10 and abs(diffY)<10):
			self.targetPos=np.array([np.random.random_sample()*800,np.random.random_sample()*600])
		
		diffX=np.sign(diffX)*-1
		diffY=np.sign(diffY)*-1
		
		self.setSpeed(diffX,diffY)
		
		
		
		diffX=self.pos[0]-Enemy.PLAYER.pos[0]
		diffY=self.pos[1]-Enemy.PLAYER.pos[1]
		self.setShooting(abs(diffX)<100 and abs(diffY)<100)
		
		super().update(dt)

class Ufo(Enemy):
	def __init__(self,pos,imgpos,speed):
		super(Ufo,self).__init__(pos,imgpos,speed)
		self.bulletType=np.array([29,0,4,4])
		self.shotTime = .6
	
	def update(self,dt):
		diffX=self.pos[0]-Enemy.PLAYER.pos[0]
		diffY=self.pos[1]-Enemy.PLAYER.pos[1]
		
		diffX=np.sign(diffX)*-1
		diffY=np.sign(diffY)*-1
		
		self.setSpeed(diffX,diffY)
		
		self.setShooting(abs(diffX)<50 and abs(diffY)<50)
		
		super().update(dt)	
	
