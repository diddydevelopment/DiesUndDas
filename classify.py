import matplotlib.pyplot as plt
import numpy.random as rnd
from math import pow
from math import sqrt
import numpy
from collections import Counter

from datapoint.Datapoint import *


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

def knN(dps, p, k):
    for ii in range(len(dps)):
        dps[ii].calcEuclidDistance(p)

    dps.sort()

    relevantPoints = dps[0:k]

    relevantClasses = [x.label for x in relevantPoints]

    count = Counter(relevantClasses)
    most = count.most_common(n=1)

    p.label = most[0][0]

    return p.label






mean1 = [4,5]
mean2 = [3,2]

scale1 = 1
scale2 = 1
numSamples = 900

dps = []
for ii in range(numSamples*2):
    dps.append(Datapoint([rnd.normal(loc=mean1[0], scale=scale1), rnd.normal(loc=mean1[1],scale=scale1)],0))
    dps.append(Datapoint([rnd.normal(loc=mean2[0], scale=scale2), rnd.normal(loc=mean2[1], scale=scale2)],1))


plot1 = plt.figure(1)
printDatapoints2d(dps,plot1)

xrange = numpy.linspace(0,10,20)
yrange = numpy.linspace(0,10,20)

toclassify = []

for xx in xrange:
    for yy in yrange:
        toclassify.append(Datapoint([xx,yy],0))

for ii in range(len(toclassify)):
    knN(dps,toclassify[ii], 10)

plot2 = plt.figure(2)
printDatapoints2d(toclassify,plot2)

plt.show()

