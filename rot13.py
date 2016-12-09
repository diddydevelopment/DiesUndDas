def rot13(s):
    cs = ""
    for b in s:
        asciib = ord(b)
        asciiv = 0
        if asciib < 110 and asciib >= 97:
            asciiv = asciib + 13
        elif asciib >= 110 and asciib <= 122 :
            asciiv = asciib - 13
        else:
            asciiv = asciib

        asciibuch = chr(asciiv)
        cs = cs + asciibuch
    return cs






satz = "verschluesselter satz"

print(rot13(satz))

print(rot13("irefpuyhrffrygre fngm"))