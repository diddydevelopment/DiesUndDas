from random import randint
import pickle

woerter = dict()
richtig = dict()
falsch = dict()

command = ""

command = input("Befehl (neu,abfrage,quiz,speichern,laden,beenden) eingeben: ")

while command != 'beenden':

    if command == 'neu': #lese neues wort in datenbank ein
        wort = input("Gebe ein Wort ein: ")
        uebersetzung = input('Gebe die Übersetzung ein: ')
        woerter[wort] = uebersetzung
        richtig[wort] = 0
        falsch[wort] = 0
        print('Wort wurde gespeichert')
    elif command == 'abfrage':
        wort = input("Gebe ein Wort ein: ")
        if wort in woerter:
            print(wort+": "+woerter[wort])
            print(wort+" wurde "+str(richtig[wort])+" mal richtig und "+str(falsch[wort])+" mal falsch abgefragt")
        else:
            print(wort+" ist nicht im Woerterbuch")
    elif command == 'quiz':
        w = list(woerter.keys());
        zufall = randint(0,len(w)-1)
        quiz = input('Was ist die Uebersetzung von '+w[zufall]+'? ')
        if quiz == woerter[w[zufall]]:
            print('Super')
            richtig[w[zufall]] = richtig[w[zufall]] +1
        else:
            print('Falsch, du Niete')
            falsch[w[zufall]] = falsch[w[zufall]] + 1
    elif command == 'quizintel':
        w = list(woerter.keys());
        wintel = []
        for w1 in w:
            gesamtAbgefragt = richtig[w1] + falsch[w1]
            anzahlInWintel = max(0,falsch[w1] - richtig[w1] + max(10-gesamtAbgefragt,0))

            wintel = wintel + [w1]*anzahlInWintel
        print(wintel)
        zufall = randint(0,len(wintel)-1)
        quiz = input('Was ist die Uebersetzung von '+wintel[zufall]+'? ')
        if quiz == woerter[wintel[zufall]]:
            print('Super')
            richtig[wintel[zufall]] = richtig[wintel[zufall]] +1
        else:
            print('Falsch, du Niete')
            falsch[wintel[zufall]] = falsch[wintel[zufall]] + 1

    elif command == 'speichern':
        with open('woerterbuch' + '.pkl', 'wb') as f:
            pickle.dump(woerter, f, pickle.HIGHEST_PROTOCOL)
        with open('num_richtig' + '.pkl', 'wb') as f:
            pickle.dump(richtig, f, pickle.HIGHEST_PROTOCOL)
        with open('num_falsch' + '.pkl', 'wb') as f:
            pickle.dump(falsch, f, pickle.HIGHEST_PROTOCOL)
    elif command == 'laden':
        with open('woerterbuch' + '.pkl', 'rb') as f:
            woerter =  pickle.load(f)
        with open('num_richtig' + '.pkl', 'rb') as f:
            richtig =  pickle.load(f)
        with open('num_falsch' + '.pkl', 'rb') as f:
            falsch =  pickle.load(f)
    else:
        print('Unbekannter Befehl')

    command = input("Befehl (neu,abfrage,quiz,beenden) eingeben: ")

print('Tschuess')