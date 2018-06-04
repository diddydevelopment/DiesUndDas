import network
import time

def scan_wifi():
    nets = []
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    s = wlan.scan()
    for ss in s:
        nets.append(ss[0].decode('utf-8'))
    return nets

def load_saved_wifis():
    networks = dict()
    try:
        fh = open('wifi_credentials.txt','r')
        csv = fh.read()
        line = csv.split('\n')
        for l in line:
            c = l.split(';')
            if len(c) == 2:
                networks[c[0]] = c[1]
        return networks
    except:
        return dict()

def connect_to_saved_ap(delay=4):
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)

    connected = False
    saved_wifis = load_saved_wifis()
    for sw in saved_wifis:
        sta_if.connect(sw, saved_wifis[sw])
        time.sleep(delay)
        if sta_if.isconnected():
            connected = True
            print('connected to ', sw)
            print(sta_if.ifconfig())
            break
        else:
            print('can not connect to ', sw)
    return connected

def enable_ap(ssid,pw,ifconfig=None):
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=ssid, password=pw)
    if ifconfig is not None:
        ap.ifconfig(ifconfig)

    print(ap.ifconfig())

def disable_ap():
    ap = network.WLAN(network.AP_IF)
    ap.active(False)

def disable_sta():
    sta = network.WLAN(network.STA_IF)
    sta.active(False)


def connect_wifi(ssid,pw,ifconfig=None):
    #deactivate access point
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)

    #connect to my wifi
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid,pw)
        while not sta_if.isconnected():
            pass
    else:
        print('is already connected')

    if ifconfig is not None:
        sta_if.ifconfig(ifconfig)
    print('network config:', sta_if.ifconfig())

