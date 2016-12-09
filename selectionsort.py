def getMinInd(l):
    minInd = 0
    minEl = l[0]
    for e in range(len(l)):
        if l[e] < minEl:
            minInd = e
            minEl = l[e]
    return minInd


def selectionSort(l):
    for e in range(len(l)-1):
        minInd = getMinInd(l[e:])

        #dreieckstausch von l[e] und l[minInd]
        t = l[e]
        l[e] = l[minInd+e]
        l[minInd+e] = t
    return l






liste = [3,2,8,6,4,7,8,9,44,3,3,5,8]

print(selectionSort(liste))