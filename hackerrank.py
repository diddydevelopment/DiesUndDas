import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def findSubOcc(str):
    rtn = 0
    while str != "":
        count = str.count(str[0])
        str = str.replace(str[0],"")
        if count > 1:
            rtn = rtn + nCr(count,2)

    return rtn


line = "aaarrrrrrrr"

lineclean = ""

for i in line:
    if line.count(i) > 1:
        lineclean = lineclean + i
found = 0
for in0 in range(len(lineclean)):
    for in1 in range(min(in0+3,len(lineclean)-1),len(lineclean)):
        if (lineclean[in0]==lineclean[in1]):
            found = found + findSubOcc(lineclean[in0+1:in1])

print(int(found % (10**9+7)))
