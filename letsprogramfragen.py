import numpy as np

from random import randint


i = randint(10,15)

liste = []

while True:
    liste.append(randint(50,60))

print(liste)

liste = [np.array([1])]*5

print(liste)

liste[3][0] = 5

print(liste)







# wort = "ab c asdf cba"
#
# wort = wort.replace(" ","")
#
# laenge = len(wort)
# i=0
# istPalindrom = True
# while i < laenge/2:
#     if wort[i] != wort[laenge - i - 1]:
#         istPalindrom = False
#     i = i + 1
#
#
# print(istPalindrom)