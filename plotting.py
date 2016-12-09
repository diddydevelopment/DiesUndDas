import matplotlib.pyplot as plt

dateihandler = open('abalone.data.csv')
inhalt = dateihandler.read()
zeilen = inhalt.split('\n')
tabelle = []
for zeile in range(len(zeilen)):
    spalten = zeilen[zeile].split(',')
    tabelle.append(spalten)
    tabelle[zeile][1:] = [float(zahl) for zahl in tabelle[zeile][1:]]

laengeF = [zeile[1] for zeile in tabelle if zeile[0] == 'F']
gewichtF = [zeile[4] for zeile in tabelle if zeile[0] == 'F']

laengeM = [zeile[1] for zeile in tabelle if zeile[0] == 'M']
gewichtM = [zeile[4] for zeile in tabelle if zeile[0] == 'M']

laengeI = [zeile[1] for zeile in tabelle if zeile[0] == 'I']
gewichtI = [zeile[4] for zeile in tabelle if zeile[0] == 'I']

plt.scatter(laengeM,gewichtM,color='red',alpha=0.2)
plt.scatter(laengeF,gewichtF,color='blue',alpha=0.2)
plt.scatter(laengeI,gewichtI,color='green',alpha=0.2)
plt.show()


pass