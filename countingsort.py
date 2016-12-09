def countingSort(l,min,max):
    sizeCounts = max-min+1
    counts = [0 for _ in range(sizeCounts)]

    for e in l:
        counts[e-min] = counts[e-min] +1

    sl = []
    for e in range(len(counts)):
        for i in range(counts[e]):
            sl.append(e+min)

    return sl




liste = [45,33,56,17,34,11,8,9,5,5,5,5,5]
print(countingSort(liste,5,100))