import numpy as np
import random as rn

import pyglet
from pyglet.window import key

from time import time

from Dir import Dir
from DisplayObject import *
from Entities import *
from Enemies import *

from globals import *


drawables = []
bullets = []
entities = []
explosions = []

left = False
right = False
up = False
down = False
shoot = False

window = pyglet.window.Window(*WINDOW_SIZE,vsync=False)
window.set_fullscreen(False)
@window.event
def on_key_press(symbol, modifiers):
	global left,right,up,down,shoot
	if symbol == key.A:
		left = True
	elif symbol == key.D:
		right = True
	elif symbol == key.W:
		up = True
	elif symbol == key.S:
		down = True
	elif symbol == key.SPACE:
		shoot = True

@window.event
def on_key_release(symbol, modifiers):
	global left,right,up,down,shoot
	if symbol == key.A:
		left = False
	elif symbol == key.D:
		right = False
	elif symbol == key.W:
		up = False
	elif symbol == key.S:
		down = False
	elif symbol == key.SPACE:
		shoot = False



class Player(Ship):
	def __init__(self,pos,imgpos,speed):
		super(Player,self).__init__(pos,imgpos,speed)

	def update(self,dt):
		x=0
		y=0

		if left:
			x=-1
		if up:
			y=1
		if right:
			x=1
		if down:
			y=-1

		self.setSpeed(x,y)
		self.setShooting(shoot)

		if self.shoot and self.lastShot+Ship.SHOTTIME < time():
			l=LaserBeam(self.pos.copy(),self.dir)
			bullets.append(l)
			drawables.append(l)
			self.lastShot = time()
			laserSound.play()

		super().update(dt)


background=pyglet.sprite.Sprite(BACKGROUND_IMAGE,0,0)
background.scale=0.5

#http://www.bfxr.net/
explosionSound = pyglet.media.StaticSource(pyglet.media.load('explosion.wav'))
laserSound = pyglet.media.StaticSource(pyglet.media.load('shoot.wav'))



p = Player(np.array([50,50]),np.array([0,0,25,25]),np.array([60,60]))
Enemy.PLAYER=p

e = Enemy(np.array([650,250]),np.array([0,25,25,25]),np.array([10,10]))
entities.append(e)

e = Enemy(np.array([650,650]),np.array([0,50,62,45]),np.array([10,10]))
e.rotate=False
entities.append(e)

stageLabel = pyglet.text.Label('Stage: ', font_name='Times New Roman', font_size=36, x=window.width // 2, y=window.height // 2, anchor_x='center', anchor_y='center')
remainingSecondsLabel = pyglet.text.Label('Remaining Time: ', font_name='Times New Roman', font_size=36, x=window.width // 2, y=window.height // 2-40, anchor_x='center', anchor_y='center')


currentStage = 0
remainingTime = -1
stageStarted = time()
stoneSpawnTime = -1
lastRockSpawned = time()


def cleanSpriteList(sprites):
	for sprite in sprites:
		if sprite.pos[0]+50 < 0 or sprite.pos[1]+50 < 0 or sprite.pos[0]-50 > window.width or sprite.pos[1]-50 > window.height:
			sprites.remove(sprite)


def initNewStage():
	global remainingTime
	global currentStage
	global stageStarted
	global stoneInterval
	global stoneSpawnTime

	#initial time between stones
	initStoneInterval = 1000
	#increase per stage
	increase_difficulty = 100
	#maximum difficulty
	hardest = 200

	#time between stones
	stoneSpawnTime = max(initStoneInterval - currentStage*increase_difficulty,hardest)

	currentStage = currentStage + 1
	stageStarted = time()



def gameLoop(dt):
	global remainingTime
	global currentStage
	global stageStarted
	global lastRockSpawned
	global stoneSpawnTime

	#update everything
	if remainingTime < 0:
		initNewStage()


	cleanSpriteList(drawables)
	cleanSpriteList(entities)

	p.update(dt)

	for e in explosions:
		if not e.update():
			explosions.remove(e)
	for e in entities:
		e.update(dt)
		
	for d in drawables:
		d.update()

	if stoneSpawnTime < time()*1000-lastRockSpawned:
		spawnRock()
		lastRockSpawned = time()*1000

	for l in bullets:
		l.update()
		for e in entities:
			if e.collides(l):
				try:
					explosions.append(Explosion(e.pos))
					explosionSound.play()
					bullets.remove(l)
					entities.remove(e)
				except:
					pass

	#draw everything
	window.clear()
	background.draw()

	for e in explosions:
		e.draw()
	for e in entities:
		e.draw()
	for d in drawables:
		d.draw()
	p.draw()
	remainingTime = STAGE_DURATION-(time()-stageStarted)
	stageLabel.text = "Stage: "+str(currentStage)
	remainingSecondsLabel.text = "Remaining Time: "+str(remainingTime)[0:5]

	stageLabel.draw()
	remainingSecondsLabel.draw()


def spawnRock():
	entities.append(Rock())


pyglet.clock.schedule_interval(gameLoop,1/60.0)
#pyglet.clock.schedule_interval(spawnRock)
#label = pyglet.text.Label('Hello, world', font_name='Times New Roman', font_size=36, x=window.width // 2, y=window.height // 2, anchor_x='center', anchor_y='center')


pyglet.app.run()
