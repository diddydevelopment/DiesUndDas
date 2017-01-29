import numpy as np
import random as rn

import pyglet
from pyglet.window import key

from time import time

from Dir import Dir

from globals import *

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

