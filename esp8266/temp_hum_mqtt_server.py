#!/usr/bin/env python
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("#")

def on_message(client, userdata, msg):
    global c
    global conn
    if msg.topic == 'temperature':
        print('temp',int(msg.payload))
        c.execute('insert into temperatures values('+str(int(msg.payload))+')')
    elif msg.topic == 'humidity':
        print('hum',int(msg.payload))
        c.execute('insert into humidities values('+str(int(msg.payload))+')')

    #save to file
    conn.commit()


import sqlite3
import os

dbfile = 'air.db'

db_exist = os.path.isfile(dbfile)
conn = sqlite3.connect(dbfile)
c = conn.cursor()

if not db_exist:
    c.execute('create table temperatures (temperature int)')
    c.execute('create table humidities (humidity int)')


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.0.235", 1883, 60)

client.loop_forever()

conn.close()
