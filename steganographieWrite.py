import numpy

def byteToStr(b,bits=8):
    safes = ""
    for biti in range(bits):
        safe = ( b & (1 << ((bits-1)-biti)))
        if safe > 0:
            safes += '1'
        else:
            safes += '0'
    return safes


def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)

image = open('stegano.bmp', 'rb')
bytes = list(image.read())

breite = int.from_bytes(bytes[18:22], byteorder='little')
hoehe = int.from_bytes(bytes[22:26], byteorder='little')

bildstart = int.from_bytes(bytes[10:14], byteorder='little')


bpp = int.from_bytes(bytes[28:30], byteorder='little')

data = numpy.zeros((breite,hoehe,3))

fill = breite * 3 % 4

for w in range(breite):
    for h in range(hoehe):
        ind = (h * (breite+fill) + w)*3 + bildstart
        data[w,h,0] = bytes[ind]
        data[w, h, 1] = bytes[ind+1]
        data[w, h, 2] = bytes[ind+2]


data = data.astype(int)

safestring = "geiler satz alter"

safestringLen = byteToStr(len(safestring),16)



safes = safestringLen;
#0001011010100110001101100011011011110110
for e in safestring:
    ei = ord(e)
    safes += byteToStr(ei)

print(safes)
curByte = 0
for e in safes:
    if e == '0':
        data[curByte % breite][curByte // breite][0] = clear_bit(data[curByte%breite][curByte//breite][0],0)
    else:
        data[curByte % breite][curByte // breite][0] = set_bit(data[curByte%breite][curByte//breite][0], 0)
    curByte = curByte +1



for w in range(breite):
    for h in range(hoehe):
        ind = (h * (breite+fill) + w)*3 + bildstart
        bytes[ind] = data[w,h,0]
        bytes[ind+1] = data[w,h,1]
        bytes[ind+2] = data[w,h,2]




safeImg = bytearray(bytes)

safeII = open('save.bmp',mode='wb')

safeII.write(safeImg)
safeII.close()