import numpy as np
import random as rn

import pyglet
from pyglet.window import key

from time import time

from DISASTER.Dir import Dir
from DISASTER.DisplayObject import *
from DISASTER.globals import *

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

