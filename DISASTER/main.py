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
gameOver=False

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

		if gameOver==False:
			self.setSpeed(x,y)
			self.setShooting(shoot)

		super().update(dt)


background=pyglet.sprite.Sprite(BACKGROUND_IMAGE,0,0)
background.scale=0.5

#http://www.bfxr.net/
explosionSound = pyglet.media.StaticSource(pyglet.media.load('explosion.wav'))
laserSound = pyglet.media.StaticSource(pyglet.media.load('shoot.wav'))

musicPlayer = pyglet.media.Player()
music = pyglet.media.load('music.wav', streaming=True)
musicPlayer.queue(music)
musicPlayer.eos_action = musicPlayer.EOS_LOOP
musicPlayer.play()


p = Player(np.array([WINDOW_SIZE[0]/2,WINDOW_SIZE[1]/2]),np.array([0,0,25,25]),60)
Enemy.PLAYER=p



stageLabel = pyglet.text.Label('Stage: ', font_name='Times New Roman', font_size=36, x=window.width // 2, y=window.height // 2, anchor_x='center', anchor_y='center')
remainingSecondsLabel = pyglet.text.Label('Remaining Time: ', font_name='Times New Roman', font_size=36, x=window.width // 2, y=window.height // 2-40, anchor_x='center', anchor_y='center')


currentStage = 0
remainingTime = -1
stageStarted = time()
stoneSpawnTime = -1
lastRockSpawned = time()
lastEnemySpawned = time()


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
	global enemySpawnTime

	#initial time between stones
	initStoneInterval = 1000
	
	initEnemyInterval = 10000
	#increase per stage
	increase_difficulty = 100
	#maximum difficulty
	hardest = 200

	#time between stones
	stoneSpawnTime = max(initStoneInterval - currentStage*increase_difficulty,hardest)
	
	enemySpawnTime = max(initEnemyInterval - currentStage*increase_difficulty,hardest)

	currentStage = currentStage + 1
	stageStarted = time()



def gameLoop(dt):
	global remainingTime
	global currentStage
	global stageStarted
	global lastRockSpawned
	global lastEnemySpawned
	global stoneSpawnTime
	global enemySpawnTime
	global gameOver

	#update everything
	if remainingTime < 0:
		initNewStage()


	cleanSpriteList(drawables)
	cleanSpriteList(entities)
	cleanSpriteList(bullets)

	p.update(dt)

	for e in explosions:
		if not e.update():
			explosions.remove(e)
	for e in entities:
		e.update(dt)
		if gameOver==False and e!=p and e.collides(p):
			explosions.append(Explosion(p.pos))
			explosionSound.play()
			gameOver=True
		
	for d in drawables:
		d.update()

	if stoneSpawnTime < time()*1000-lastRockSpawned:
		spawnRock()
		lastRockSpawned = time()*1000
		
	if enemySpawnTime < time()*1000-lastEnemySpawned:
		spawnEnemy()
		lastEnemySpawned = time()*1000


	for l in bullets:
		l.update()
		for e in entities:
			if l.targetType=='Rest' and l.collides(e):
				try:
					explosions.append(Explosion(e.pos))
					explosionSound.play()
					bullets.remove(l)
					entities.remove(e)
				except:
					pass
		if gameOver==False and l.targetType=='Player' and l.collides(p):
			explosions.append(Explosion(p.pos))
			explosionSound.play()
			gameOver=True
			
			
	#draw everything
	window.clear()
	background.draw()

	for e in explosions:
		e.draw()
	for e in entities:
		e.draw()
	for d in drawables:
		d.draw()
	if gameOver==False:
		p.draw()
	remainingTime = STAGE_DURATION-(time()-stageStarted)
	stageLabel.text = "Stage: "+str(currentStage)
	remainingSecondsLabel.text = "Remaining Time: "+str(remainingTime)[0:5]
	
	if gameOver:
		if(currentStage<2):
			stageLabel.text = "GAME OVER SUCKER! Stage " +str(currentStage)
		elif (currentStage<4):
			stageLabel.text = "KEEP GOING! Stage " +str(currentStage)
		elif (currentStage<8):
			stageLabel.text = "YOU ARE TOO GOOD! Stage  " +str(currentStage)
			
		

	stageLabel.draw()
	remainingSecondsLabel.draw()


def spawnRock():
	entities.append(Rock())

def spawnBullet(s,l):
    bullets.append(l)
    drawables.append(l)
    
def spawnEnemy():
	if(np.random.random_sample()<0.2):
		e = Mothership(np.array([350,250]),np.array([0,50,62,45]),3)
	else:
		e = Ufo(np.array([0,0]),np.array([0,25,25,25]),10)
	e.randomStartPos()
	entities.append(e)
	
	
    
Ship.addBullet=spawnBullet

pyglet.clock.schedule_interval(gameLoop,1/60.0)
#pyglet.clock.schedule_interval(spawnRock)
#label = pyglet.text.Label('Hello, world', font_name='Times New Roman', font_size=36, x=window.width // 2, y=window.height // 2, anchor_x='center', anchor_y='center')


pyglet.app.run()
