import urllib.request as ul
import re


def getbaseurl(url):
    regex = list(re.finditer('[^/]/[^/]', url))
    if len(regex) == 0:
        return url
    else:
        return url[:regex[0].start()+1]

def getFilename(url):
    return url[url.rfind('/') + 1:]

url = 'http://www.capefearit.com'
urlBase = getbaseurl(url)
fileEx = 'jpg'
saveFolder = 'files'



#import urllib #bei manchen systemen
f = ul.urlopen(url)
html = str(f.read())


aId = [(a.start(), a.end()) for a in list(re.finditer('<a[^>]*', html))]

ahrefs =  [html[l[0]:l[1]] for l in aId]

for l in ahrefs:
    print(l)

linksId = [(a.start(), a.end()) for a in list(re.finditer('[^"]*\.'+fileEx, html))]

links =  [html[l[0]:l[1]] for l in linksId]


for l in links:
    if l.startswith('//'):
        l = 'http://'+l[2:]
    elif l.startswith('http://'):
        pass
    elif l.startswith('/'):
        l = urlBase+l
    else:
        l = urlBase+'/'+l
    try:
        ul.urlretrieve(l, saveFolder+'/'+getFilename(l))
    except Exception:
        print('can\'t get link '+l)
