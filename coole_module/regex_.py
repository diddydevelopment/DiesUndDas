import re


satz = "hallo anna, ich wohne in 33602 Bielefeld, wohnst du immernoch in 21499 Berlin?"
regex = re.compile('[0-9]{5}')
print(regex.findall(satz))

satz2 = "Hallo Otto, ich bin im Auto. Kommst du bitte zu mir auf den Beifahrersitz?"
regex2 = re.compile('[^\.\!\?][ ]+[A-Z][a-z]+')

nomen = regex2.findall(satz2)

for n in nomen:
    print(n[n.index(" ")+1:])