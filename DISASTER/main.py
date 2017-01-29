import numpy as np
import random as rn

import pyglet
from pyglet.window import key

from time import time


WINDOW_SIZE = (800,600)
GFX = pyglet.image.load('gfx.png')
BACKGROUND_IMAGE = pyglet.image.load('spacePlosion.png')
background=pyglet.sprite.Sprite(BACKGROUND_IMAGE,0,0)
background.scale=0.5

SPRITE_SIZE = 25

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

class Dir():
    up=0
    down=1
    left=2
    right=3
    upright=4
    downright=5
    downleft=6
    upleft=7


class DisplayObject():
    def __init__(self,pos,imgpos):
        self.pos = pos
        subimg = GFX.get_region(x=imgpos[0],y=GFX.height-imgpos[1]-imgpos[3],width=imgpos[2],height=imgpos[3])
        subimg.anchor_x = subimg.width//2
        subimg.anchor_y = subimg.height//2
        self.sprite = pyglet.sprite.Sprite(subimg)
        self.h = self.sprite.height
        self.w = self.sprite.width

    def draw(self):
        self.sprite.x = self.pos[0]
        self.sprite.y = self.pos[1]
        self.sprite.draw()
    def move(self, d):
        self.pos += d
    def collides(self,other):
        pos = [self.pos[0]-self.w/2,self.pos[1]-self.h/2]
        opos = [other.pos[0] - other.w / 2, other.pos[1] - other.h / 2]
        if pos[0] + self.w < opos[0] or opos[0]+other.w < pos[0] or pos[1] + self.h < opos[1] or opos[1]+other.h < pos[1]:
                return False
        return True



class Entity(DisplayObject):
    def __init__(self,pos,imgpos,speed):
        super(Entity,self).__init__(pos,imgpos)
        self.speed = speed
    def update(self):
        raise NotImplementedError('Please implement update method')


class Rock(DisplayObject):
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
        super(Rock, self).__init__(pos, [50,0,25,25])

    def update(self):
        self.move(self.curSpeed)
        if self.dir == Dir.down and self.pos[1] < -SPRITE_SIZE:
            self.pos[1] = WINDOW_SIZE[1]
        elif self.dir == Dir.up and self.pos[1] > WINDOW_SIZE[1]:
            self.pos[1] = -SPRITE_SIZE
        elif self.dir == Dir.right and self.pos[0] > WINDOW_SIZE[0]:
            self.pos[0] = -SPRITE_SIZE
        elif self.dir == Dir.left and self.pos[0] < SPRITE_SIZE:
            self.pos[0] = WINDOW_SIZE[0]


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

p = Player(np.array([50,50]),np.array([0,0,25,25]),np.array([10,10]))



class LaserBeam(DisplayObject):
    SPEED = 30
    def __init__(self,pos,dir):
        super(LaserBeam,self).__init__(pos,np.array([25,0,4,4]))
        self.dir = dir
        d = [0, 0]
        if self.dir == Dir.down or self.dir == Dir.downleft or self.dir == Dir.downright:
            d[1] = -LaserBeam.SPEED
        if self.dir == Dir.up or self.dir == Dir.upleft or self.dir == Dir.upright:
            d[1] = LaserBeam.SPEED
        if self.dir == Dir.left or self.dir == Dir.downleft or self.dir == Dir.upleft:
            d[0] = -LaserBeam.SPEED
        if self.dir == Dir.right or self.dir == Dir.upright or self.dir == Dir.downright:
            d[0] = LaserBeam.SPEED
        self.d = d
    def update(self):
        self.move(self.d)




def gameLoop(dt):
    p.update(dt)
    for r in rocks:
        r.update()
    for il,l in enumerate(laserbeams):
        l.update()
        for ir,r in enumerate(rocks):
            if r.collides(l):
                del laserbeams[il]
                del rocks[ir]


    window.clear()
    background.draw()
    
    for r in rocks:
        r.draw()
    for l in laserbeams:
        l.draw()

    p.draw()
    #label.draw()

def spawnRock(dt):
    rocks.append(Rock())
pyglet.clock.schedule_interval(gameLoop,1/60.0)
pyglet.clock.schedule_interval(spawnRock,2)
#label = pyglet.text.Label('Hello, world', font_name='Times New Roman', font_size=36, x=window.width // 2, y=window.height // 2, anchor_x='center', anchor_y='center')




pyglet.app.run()
