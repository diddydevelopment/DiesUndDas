def lastManStanding(n,k,p):
    leute = list(range(n))
    while len(leute) != 1:
        del(leute[p])
        p = (p + k-1) % len(leute)
    return leute[0]


def lastManStanding2(n,k,p):
    leute = list(range(n))
    while len(leute) != 1:
        del(leute[p])
        p = (p + k) % len(leute)
    return leute[0]

n = 7
k = 4
p = 2

print(lastManStanding(n,k,p))
print(lastManStanding2(n,k,p))
#print(lastManStanding2(10,3,9))
print(lastManStanding(34565,10,23534))