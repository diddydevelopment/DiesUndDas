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

	def update(self,dt):
		x=np.sign(self.pos[0]-Enemy.PLAYER.pos[0])*-1
		y=np.sign(self.pos[1]-Enemy.PLAYER.pos[1])*-1
		
		self.setSpeed(x,y)
		
		#self.setShooting(shoot)
        
		#if self.shoot and self.lastShot+Ship.SHOTTIME < time():
		#	laserbeams.append(LaserBeam(self.pos.copy(),self.dir))
		#	self.lastShot = time()
        
		super().update(dt)
