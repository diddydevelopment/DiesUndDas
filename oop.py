class Rechteck:
    def __init__(self,laenge,breite):

        self.myLaenge = laenge
        self.myBreite = breite

        print('rechteck erstellt')


    def printRechteck(self):
        print('Das Rechteck hat die Laenge '+str(self.myLaenge)+' und die Breite '+str(self.myBreite))

    def calcUmfang(self):
        return 2*self.myBreite + 2*self.myLaenge

    def calcFI(self):
        print('recheckmethode')
        return self.myBreite * self.myLaenge

    def hasBiggerFI(self,other):
        selfFI = self.calcFI()
        otherFI = other.calcFI()
        return selfFI > otherFI


class Quadrat(Rechteck):
    def __init__(self,seite):
        super(Quadrat,self).__init__(seite,seite)

    def calcUmfang(self):
        return 4 * self.myLaenge


quad1 = Quadrat(5)

print(quad1.calcFI())

recht1 = Rechteck(4,6)

print(recht1.calcFI())