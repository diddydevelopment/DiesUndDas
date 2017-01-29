import numpy as np
import random as rn

import pyglet
from pyglet.window import key

from time import time

from Dir import Dir
from DisplayObject import *
from Entities import *

from globals import *


rocks = []
laserbeams = []

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



class Player(Entity):
    SHOTTIME = .1
    def __init__(self,pos,imgpos,speed):
        super(Player,self).__init__(pos,imgpos,speed)
        self.dir = Dir.up
        self.lastShot = time()


    def update(self,dt):
        dx = 0
        dy = 0
        if left:
            dx = dx - self.speed[0]
            self.sprite.rotation = 270
            self.dir = Dir.left
        if right:
            dx = dx + self.speed[0]
            self.sprite.rotation = 90
            self.dir = Dir.right

        if up:
            dy = dy + self.speed[1]
            self.sprite.rotation = 0
            self.dir = Dir.up

        if down:
            dy = dy - self.speed[1]
            self.sprite.rotation = 180
            self.dir = Dir.down

        if up and right:
            self.sprite.rotation = 45
            self.dir = Dir.upright

        if down and right:
            self.sprite.rotation = 135
            self.dir = Dir.downright

        if down and left:
            self.sprite.rotation = 225
            self.dir = Dir.downleft

        if up and left:
            self.sprite.rotation = 315
            self.dir = Dir.upleft

        self.move(np.array([dx,dy]))

        if shoot and self.lastShot+Player.SHOTTIME < time():
            laserbeams.append(LaserBeam(self.pos.copy(),self.dir))
            self.lastShot = time()


background=pyglet.sprite.Sprite(BACKGROUND_IMAGE,0,0)
background.scale=0.5

p = Player(np.array([50,50]),np.array([0,0,25,25]),np.array([10,10]))


stageLabel = pyglet.text.Label('Stage: ', font_name='Times New Roman', font_size=36, x=window.width // 2, y=window.height // 2, anchor_x='center', anchor_y='center')
remainingSecondsLabel = pyglet.text.Label('Remaining Time: ', font_name='Times New Roman', font_size=36, x=window.width // 2, y=window.height // 2-40, anchor_x='center', anchor_y='center')


currentStage = 0
remainingTime = -1
stageStarted = time()

def cleanSpriteList(sprites):
    for sprite in sprites:
        if sprite.pos[0]+50 < 0 or sprite.pos[1]+50 < 0 or sprite.pos[0]-50 > window.width or sprite.pos[1]-50 > window.height:
            sprites.remove(sprite)
            print("sprite removed")


def gameLoop(dt):
    global remainingTime
    global currentStage
    global stageStarted

    #update everything
    if remainingTime < 0:
        currentStage = currentStage+1
        stageStarted = time()


    cleanSpriteList(rocks)
    cleanSpriteList(laserbeams)

    p.update(dt)
    for r in rocks:
        r.update()
    for il,l in enumerate(laserbeams):
        l.update()
        for ir,r in enumerate(rocks):
            if r.collides(l):
                del laserbeams[il]
                del rocks[ir]


    #draw everything
    window.clear()
    background.draw()
    
    for r in rocks:
        r.draw()
    for l in laserbeams:
        l.draw()
    p.draw()
    remainingTime = STAGE_DURATION-(time()-stageStarted)
    stageLabel.text = "Stage: "+str(currentStage)
    remainingSecondsLabel.text = "Remaining Time: "+str(remainingTime)[0:5]

    stageLabel.draw()
    remainingSecondsLabel.draw()


def spawnRock(dt):
    rocks.append(Rock())


pyglet.clock.schedule_interval(gameLoop,1/60.0)
pyglet.clock.schedule_interval(spawnRock,2)
#label = pyglet.text.Label('Hello, world', font_name='Times New Roman', font_size=36, x=window.width // 2, y=window.height // 2, anchor_x='center', anchor_y='center')


pyglet.app.run()
