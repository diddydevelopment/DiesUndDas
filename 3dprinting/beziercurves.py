import numpy as np
from scipy.misc import comb


def bezier(points,ns=20):
    points = np.array(points)
    n = len(points)
    step = 1.0/ns
    rtn_points = []
    for t in np.arange(0,1+step,step):
        c = np.array([0,0],np.float)
        for i,p in enumerate(points):
            c += comb(n-1,i) * t**i * (1-t)**(n-i-1) * p
        rtn_points.append(c)
    return np.array(rtn_points)

bp = bezier([[0,0],[1,0],[1,5]],20)

rtn = '['

for p in bp:
    rtn += '['+str(p[0])+','+str(p[1])+'],'

rtn += ']'

print(rtn)