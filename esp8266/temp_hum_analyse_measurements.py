import sqlite3
import os
import numpy as np
import matplotlib.pyplot as plt
dbfile = 'air.db'

db_exist = os.path.isfile(dbfile)
conn = sqlite3.connect(dbfile)
c = conn.cursor()


temps = c.execute('SELECT * from temperatures')
temps = np.array(temps.fetchall())
hums = c.execute('SELECT * from humidities')
hums = np.array(hums.fetchall())


f, ax = plt.subplots(2,1,True)
ax[0].plot(temps[:,0])
ax[1].plot(hums[:,0])
plt.show()