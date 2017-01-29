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



class Mothership(Enemy):
	def __init__(self,pos,imgpos,speed):
		super(Mothership,self).__init__(pos,imgpos,speed)
		self.targetPos = np.array(pos,np.float32)
	
	def update(self,dt):
		
		diffX=self.pos[0]-self.targetPos[0]
		diffY=self.pos[1]-self.targetPos[1]
		
		x=np.sign(diffX)*-1
		y=np.sign(diffY)*-1
		
		self.setSpeed(x,y)
		
		if(abs(diffX)<10 and abs(diffY)<10):
			self.targetPos=np.array([np.random.random_sample()*800,np.random.random_sample()*600])
		
		
		diffX=self.pos[0]-Enemy.PLAYER.pos[0]
		diffY=self.pos[1]-Enemy.PLAYER.pos[1]
		self.setShooting(abs(diffX)<500 and abs(diffY)<500)
		
		super().update(dt)

class Ufo(Enemy):
	def __init__(self,pos,imgpos,speed):
		super(Ufo,self).__init__(pos,imgpos,speed)
		
	
	def update(self,dt):
		diffX=self.pos[0]-Enemy.PLAYER.pos[0]
		diffY=self.pos[1]-Enemy.PLAYER.pos[1]
		
		x=np.sign(diffX)*-1
		y=np.sign(diffY)*-1
		
		self.setSpeed(x,y)
		
		self.setShooting(abs(diffX)<100 and abs(diffY)<100)
		
		super().update(dt)	
	
