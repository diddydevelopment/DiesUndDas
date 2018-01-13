import nltk

#nltk.download('all')

from nltk.stem.snowball import SnowballStemmer

print(", ".join(SnowballStemmer.languages))

stemmer = SnowballStemmer('german')

for x in ['gehe','anrufst','haben']:
    print(stemmer.stem(x))