def mergesort(l1,l2):
    in1 = 0
    in2 = 0

    merged = []

    while True:
        if l1[in1] < l2[in2]:
            merged.append(l1[in1])
            in1 = in1+1
        else:
            merged.append(l2[in2])
            in2 = in2+1

        if in1 == len(l1):
            merged.extend(l2[in2:])
            break
        elif in2 == len(l2):
            merged.extend(l1[in1:])
            break
    return merged



list1 = [3,5,6,7,8,9,11,32,664,887,999]
list2 = [1,2,3,4,65,67,69,111,345,444,555,666,777]

print(mergesort(list1,list2))