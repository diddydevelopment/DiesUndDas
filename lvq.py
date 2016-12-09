import matplotlib.pyplot as plt
import numpy.random as rnd
from math import pow
from math import sqrt
import numpy
from collections import Counter
from datapoint.Datapoint import *

from matplotlib.backends.backend_pdf import PdfPages

programmieren alter dasaist voll geildiddsyideveljijkjmnhnlnlksdnvinkijlijgi5rtgtrggrezrure6e5wt6z7u8i87z6t5432123t6duyydevelopment ist der geilste ficker auf der welt alter boahhhhmaaaan ey

def lvq_train(traindp):
    pp = PdfPages('lvq_training.pdf')
    plotpdf = plt.figure(10)
    learningrate = 0.05

    #initializing of weight vectors
    classes = []
    prototypes = []
    for datapoint in traindp:
        if datapoint.label not in classes:
            classes.append(datapoint.label)
            prototypes.append(datapoint)

    #go through train set and move prototypes
    for datapoint in traindp:
        for prototype in prototypes:
            prototype.calcEuclidDistance(datapoint)

        prototypes.sort()

        if prototypes[0].label == datapoint.label: #correct classified (move prototype towards)
            prototypes[0].changePosTowards(datapoint,learningrate)
        else: #incorrect classified datapoint (move prototype away)
            prototypes[0].changePosAway(datapoint,learningrate)
        printDatapoints2d(prototypes, plt.figure())
        plt.xlim([0, 5])
        plt.ylim([0, 5])
        pp.savefig()

    pp.close()
    return prototypes


def lvq_classify():
    pass




mean1 = [4,5]
mean2 = [3,2]

scale1 = 1
scale2 = 1
numSamples = 5

dps = []
for ii in range(numSamples*2):
    dps.append(Datapoint([rnd.normal(loc=mean1[0], scale=scale1), rnd.normal(loc=mean1[1],scale=scale1)],0))
    dps.append(Datapoint([rnd.normal(loc=mean2[0], scale=scale2), rnd.normal(loc=mean2[1], scale=scale2)],1))

plot1 = plt.figure(1)
printDatapoints2d(dps,plot1)

prototypes = lvq_train(dps)

plot2 = plt.figure(2)

printDatapoints2d(prototypes,plot2)



xrange = numpy.linspace(0,10,20)
yrange = numpy.linspace(0,10,20)

toclassify = []

for xx in xrange:
    for yy in yrange:
        toclassify.append(Datapoint([xx,yy],0))

#for ii in range(len(toclassify)):
#    knN(dps,toclassify[ii], 10)

plot3 = plt.figure(3)
printDatapoints2d(toclassify,plot3)

#plt.show()

