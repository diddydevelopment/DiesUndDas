from threading import Thread
import random


class MeinThread(Thread):
    def run(self):
        self.killed = False
        while not self.killed:
            print('halloThread')

    def kill(self):
        self.killed = True


t = MeinThread()

t.start()


for _ in range(2000):
    print('rechne')


t.kill()