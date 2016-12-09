from random import randint
import pickle



woerter = dict()

richtig = dict()
falsch = dict()


command = ""

command = input('Behfehl eingeben: ')

while command != 'beenden':

    if command == 'neu':
        wort = input('Bitte gebe ein neues Wort ein: ')
        uebersetzung = input('Bitte gebe die Uebersetzung ein: ')
        woerter[wort] = uebersetzung
        richtig[wort] = 0
        falsch[wort] = 0
        print('Wort wurde gespeichert')
    elif command == 'abfrage':
        wort = input('Bitte gebe ein Wort ein: ')
        if wort in woerter:
            print(wort+': '+woerter[wort])
            print(wort+' wurde '+str(richtig[wort])+' mal richtig und '+str(falsch[wort])+' mal falsch eingegeben')
        else:
            print('Wort ist nicht in Woerterbuch, bitte eintragen mit neu')
    elif command == 'quiz':
        w = list(woerter.keys())
        wintel = []
        for w1 in w:
            gesamtAbgefragt = richtig[w1] + falsch[w1]
            anzahlInWintel = max(0,falsch[w1]-richtig[w1]+max(10-gesamtAbgefragt,0))

            wintel = wintel + [w1]*anzahlInWintel

        #debug
        #print(wintel)

        zufall = randint(0,len(wintel)-1)
        abfrageWort = wintel[zufall]
        abfrage = input('Was ist die Uebersetzung von: '+abfrageWort+'?')
        if abfrage == woerter[abfrageWort]:
            print('Richtig!!')
            richtig[abfrageWort] = richtig[abfrageWort] +1
        else:
            print('Falsch, du Niete')
            falsch[abfrageWort] = falsch[abfrageWort] + 1

    elif command == 'speichern':
        with open('woerterbuch.pkl','wb') as f:
            pickle.dump(woerter,f,pickle.HIGHEST_PROTOCOL)
        with open('num_richtig.pkl', 'wb') as f:
            pickle.dump(richtig, f, pickle.HIGHEST_PROTOCOL)
        with open('num_falsch.pkl', 'wb') as f:
            pickle.dump(falsch, f, pickle.HIGHEST_PROTOCOL)
        print('gespeichert')
    elif command == 'laden':
        with open('woerterbuch.pkl', 'rb') as f:
            woerter = pickle.load(f)
        with open('num_richtig.pkl', 'rb') as f:
            richtig = pickle.load(f)
        with open('num_falsch.pkl', 'rb') as f:
            falsch = pickle.load(f)
        print('geladen')

    else:
        print('Unbekannter Befehl')

    command = input('Behfehl eingeben: ')


print('Fertig, danke für die Benutzung')