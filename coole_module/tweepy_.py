from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream

from textblob_de import TextBlobDE

from coole_module.tweepy_keys import *



class StdOutListener(StreamListener):

    def __init__(self):
        pass

    def on_data(self, data):
        print(data)
    def on_error(self, status_code):
        print(status_code)

class KanzlerListener(StreamListener):

    def __init__(self):
        self.anzahl = 0
        self.meinungen = 0

    def on_data(self, data):
        pol = TextBlobDE(str(data)).sentiment.polarity
        self.meinungen += pol
        self.anzahl += 1

        #print(data)
        #print(pol)

        print(self.anzahl)
        print(self.meinungen/self.anzahl)



    def on_error(self, status_code):
        print(status_code)



keywords = ['schulz','spd']

l = KanzlerListener()

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

stream = Stream(auth,l)

stream.filter(track=keywords)

#merkel: 0.08
#schulz: 0.14