import gc
import webrepl
import network

webrepl.start()
gc.collect()

#deactivate access point
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

sta_if = network.WLAN(network.STA_IF)
sta_if.active()
#False
sta_if.active(True)
# sta_if.connect('diddydevelopment', 'InternetOfTh1ngs')
sta_if.connect('UPCDEF486B', '82uZtdmvxvpr')
sta_if.isconnected()
#True

#get ip address
sta_if.ifconfig()

# sta_if.ifconfig(('192.168.101.234', '255.255.255.0', '192.168.101.1', '192.168.101.1'))
sta_if.ifconfig(('192.168.0.241', '255.255.255.0', '192.168.0.1', '192.168.0.1'))

print('network config:', sta_if.ifconfig())

#everything in a list for easy copy past:
# a = ['import gc\n', 'import webrepl\n', 'import network\n', 'webrepl.start()\n', 'gc.collect()\n', 'ap_if = network.WLAN(network.AP_IF)\n', 'ap_if.active(False)\n', 'sta_if = network.WLAN(network.STA_IF)\n', 'sta_if.active()\n', 'sta_if.active(True)\n', "sta_if.connect('UPCDEF486B', '82uZtdmvxvpr')\n", "sta_if.ifconfig(('192.168.0.241', '255.255.255.0', '192.168.0.1', '192.168.0.1'))\n", "print('network config:', sta_if.ifconfig())\n"]



import led_strip
np = led_strip.get_np()
led_strip.animation_rand_rect(np,50,200)


import led_strip
from font_5x3 import font
np = led_strip.get_np()
led_strip.running_text(np,'this is a default text - change it in code bro ;)',font,pos_y=0,col=[50,0,0,0],increment=1,sleep_ms=0)
