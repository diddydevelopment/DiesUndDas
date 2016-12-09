import random


def isSorted(l):
    former = l[0]

    for e in l:
        if e < former:
            return False
        former = e
    return True


def doTheBogo(l):
    nl = []

    while not l == []:
        zufall = random.randint(0,len(l)-1)
        nl.append(l[zufall])
        del(l[zufall])

    return nl



def bogoSort(l):
    i = 0
    while not isSorted(l):
        l = doTheBogo(l)
        i = i +1
    print("Bogosort hat "+str(i)+" mal gebogot")
    return l

liste = [5,2,7,9,5,3,3,2,6,8,9,5,3,2,5,7,9]
print(bogoSort(liste))