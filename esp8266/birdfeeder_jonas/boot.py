# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
import webrepl
webrepl.start()
gc.collect()

import network

def create_wifi():
    ap = network.WLAN(network.AP_IF) # create access-point interface
    ap.active(True)         # activate the interface
    ap.config(essid='feedyBirdLess') # set the ESSID of the access point
    ap.ifconfig(('192.168.0.233', '255.255.255.0', '192.168.0.1', '192.168.0.1'))

def connect_wifi():

    #deactivate access point
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)

    #connect to my wifi
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True) 
        sta_if.connect('','')
        while not sta_if.isconnected():
            pass
    sta_if.ifconfig(('192.168.0.233', '255.255.255.0', '192.168.0.1', '192.168.0.1'))
    print('network config:', sta_if.ifconfig())

#create_wifi()
connect_wifi()
