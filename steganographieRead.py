import numpy

image = open('save.bmp', 'rb')
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

datastring = ''

for h in range(hoehe):
    for w in range(breite):
        if data[w][h][0] & 1 == 1:
            datastring = datastring + '1'
        else:
            datastring = datastring + '0'

print(datastring)

#first 2 bytes are length of string

length = int(datastring[0:16],2)
print('safestring has length '+str(length))


for ii in range(length):
    #print(datastring[ii*8:ii*8+8])
    print(chr(int(datastring[16+ii*8:16+ii*8+8],2)))

