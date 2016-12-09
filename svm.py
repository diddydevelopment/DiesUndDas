#
#
#
#
#
#
#
#3          b
#
#
#2              b
#
#
#1          a
#--------------------------------------------------
#   -1  0   1   2   3   4

import numpy as np
from cvxpy import *
import matplotlib.pyplot as plt
x = np.array([[1,1],[1.5,1.5],[2,2],[1,3]])
y = np.array([1,1,-1,-1])

w = Variable(len(x[0]))
b = Variable()
slack = Variable(len(x))
c = 0.5

##without slack
#mini = 0.5*square(norm(w))
#const = mul_elemwise(y, x*w + b)
#constraints = [const >= 1]

mini = 0.5*square(norm(w))+c*sum_entries(slack)
const = mul_elemwise(y, x*w + b)
constraints = [const >= 1 - slack,slack >= 0]

obj = Minimize(mini)
prob = Problem(obj,constraints)
prob.solve()

print ("status:", prob.status)
print ("optimal value", prob.value)
print ("optimal var", w.value, b.value)
print ("slack",slack.value)
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.grid()
plt.scatter(x[:,0],x[:,1])
plt.plot([0,10*-w[1].value],[b.value,b.value+10*w[0].value])
plt.show()

#
# from cvxpy import *
#
# x = [[1,1],[2,2],[1,3]]
# y = [1,-1,-1]
#
# alphas = Variable(3)
#
#
#
# summe = 0
# for v in alphas:
#     summe = summe + v
#
# summe2 = 0
# for i in range(len(y)):
#     for j in range(len(y)):
#         summe2 = summe2 + y[i] *y[j] * alphas[i] * alphas[j] * (x[i][0]*x[j][0]+x[i][1]*x[j][1])
#
# summegesamt = summe - 0.5 * summe2
# const = 0
#
# for i in range(len(y)):
#     const = const + y[i]*alphas[i]
#
# constraints = [const == 0]
#
# obj = Maximize(summegesamt)
# prob = Problem(obj,constraints)
# prob.solve()