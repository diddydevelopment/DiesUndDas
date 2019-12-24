# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
import webrepl
import network
import helper_wifi



webrepl.start()
gc.collect()


connected = helper_wifi.connect_to_saved_ap()
print(connected)
if not connected:
	helper_wifi.disable_sta()
	helper_wifi.enable_ap('esp_ap','password')
	import http # evtl wieder einruecken
	http.http_listen()
