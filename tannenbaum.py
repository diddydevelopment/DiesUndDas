  #
 ###
#####
  #

import random

hoehe = 15

for h in list(range(hoehe))+[0]:
    abstand = hoehe-h
    zeile = ''
    for i in range(h*2+1):
        zeile += '#' if random.random() < 0.8 else '*'
    print( (' '*abstand)+ zeile + (' '*abstand) )