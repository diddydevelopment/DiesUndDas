def insertionSort(l):
    sl = []
    for e in l:
        inserted = False
        for sle in range(len(sl)):
            if sl[sle] > e:
                sl.insert(sle,e)
                inserted = True
                break
        if inserted == False:
            sl.append(e)
    return sl


liste = [5,4,1,2,3]

print(insertionSort(liste))