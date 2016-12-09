class Rectangle:
    def __init__(self,laenge,breite):
        self.laenge = laenge
        self.breite = breite

    def flaecheninhaltBerechnen(self):
        return self.laenge * self.breite

    def umfangBerechnen(self):
        return 2*self.laenge+2*self.breite

    def informationAusgeben(self):
        print('Rechteck mit Laenge '+str(self.laenge)+' und Breite '+str(self.breite))

    def hatGroesserenFlaecheninhalt(self,r):
        return self.flaecheninhaltBerechnen() > r.flaecheninhaltBerechnen()

class Quad(Rectangle):
    def __init__(self,laenge):
        super(Quad,self).__init__(laenge,laenge)


q1 = Quad(5)
r1 = Rectangle(6,5)

if r1.hatGroesserenFlaecheninhalt(q1):
    print('r1 hat groesseren FI als q1')
else:
    print('q1 hat groesseren FI als r1')


print(r1.flaecheninhaltBerechnen())

q1.informationAusgeben()
