
def getPivot(l):
    # el = [l[0], l[len(l)//2], l[-1]]
    #
    # if el[0] <= el[1] <= el[2]:
    #     return el[1]
    # elif el[1] <= el[0] <= el[2]:
    #     return el[0]
    # else:
    #     return el[2]
    return l[0]


def quicksort(l):
    if len(l) == 1 or len(l) == 0:
        return l

    pivot = getPivot(l)
    lesser = [e for e in l if e < pivot]
    greater = [e for e in l if e > pivot]
    equal = [e for e in l if e == pivot]
    return quicksort(lesser)+equal+quicksort(greater)



sortList = [6,2,4,8,4]

sorted = quicksort(sortList)

print(sorted)