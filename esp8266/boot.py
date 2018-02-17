# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
import webrepl
webrepl.start()
gc.collect()

def connect_wifi():
    import network

    #deactivate access point
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)

    #connect to my wifi
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('UPCDEF486B', '82uZtdmvxvpr')
        while not sta_if.isconnected():
            pass
    else:
        print('is already connected')

    sta_if.ifconfig(('192.168.0.234', '255.255.255.0', '192.168.0.1', '192.168.0.1'))
    print('network config:', sta_if.ifconfig())


connect_wifi()
