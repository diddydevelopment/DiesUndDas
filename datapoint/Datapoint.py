import matplotlib.pyplot as plt
import numpy.random as rnd
from math import pow
from math import sqrt
from operator import sub
from operator import add
from operator import mul
import numpy
from collections import Counter


class Datapoint:


    def __init__(self,params,label=None):
        self.params = params
        self.label = label

    def calcEuclidDistance(self,p):
        assert(len(self.params) == len(p.params))

        squaredSum = 0;
        for ii in range(len(self.params)):
            squaredSum += pow(p.params[ii] - self.params[ii],2)
        squaredSum = sqrt(squaredSum)
        self.distanceToPoint = squaredSum

    def __lt__(self, other):
        return self.distanceToPoint < other.distanceToPoint

    def directionTo(self,other):
        return map(sub,other.params,self.params)

    def changePosTowards(self,other,learningrate):
        vec = map(mul,self.directionTo(other),[learningrate]*len(self.params))
        self.params = list(map(add,self.params,vec))

    def changePosAway(self,other,learningrate):
        vec = map(mul,other.directionTo(self),[learningrate]*len(self.params))
        self.params = list(map(add,self.params,vec))

def getClass(dp,numClass):
    x0 = [x.params[0] for x in dp if x.label == numClass]
    y0 = [x.params[1] for x in dp if x.label == numClass]
    return [x0,y0]



def printDatapoints2d(dp,plot):

    colors = ['red','green','blue','orange','yellow','pink','brown','gray']

    cls = []
    count = 0
    while True:
        newClass = getClass(dp,count)
        if newClass == [[],[]]:
            break
        else:
            cls.append(newClass)
            count = count + 1


    for ii in range(len(cls)):
        plt.scatter(cls[ii][0],cls[ii][1], color=colors[ii], alpha=0.8)

    plot.show()