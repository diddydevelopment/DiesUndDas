import gc
import webrepl
import network
webrepl.start()
gc.collect()
\
#deactivate access point
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

sta_if = network.WLAN(network.STA_IF)
sta_if.active()
#False
sta_if.active(True)
# sta_if.connect('diddydevelopment', 'InternetOfTh1ngs')
sta_if.connect('FRITZ!Box 7490', 'ErnstLorenz1987!')
sta_if.isconnected()
#True

#get ip address
sta_if.ifconfig()

# sta_if.ifconfig(('192.168.101.234', '255.255.255.0', '192.168.101.1', '192.168.101.1'))
# sta_if.ifconfig(('192.168.0.240', '255.255.255.0', '192.168.0.1', '192.168.0.1'))
sta_if.ifconfig(('192.168.178.120', '255.255.255.0', '192.168.178.1', '192.168.178.1'))


print('network config:', sta_if.ifconfig())
