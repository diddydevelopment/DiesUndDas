import requests

r = requests.get('http://google.com')

print(r.text)

f = open('google.html','w')
f.write(r.text)

f.flush()
f.close()

s = 0

while s < 100:
    get_parameters = {'q':'irgendwas','start':str(s)}
    r2 = requests.get('https://www.google.de/search',get_parameters)

    print(r2.text)

    f = open('google_suche_'+str(s)+'.html','w')
    f.write(r2.text)

    f.flush()
    f.close()
    s = s + 10
