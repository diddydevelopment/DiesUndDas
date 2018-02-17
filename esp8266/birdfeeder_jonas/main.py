import alarm
from machine import Pin
from machine import RTC
import time
import server

print('main start')

def birdFeeder():
    import servoTest
    servoTest.run(5)

p1 = Pin(2, Pin.OUT)  

if(alarm.init()):
    print('alarm triggered')
    p1.off()
    
    f = open('alarm.log','a')
    f.write(str(RTC().datetime()) + ": alarm triggered \n")
    f.close()
    
    #birdFeeder()
    
    time.sleep_ms(60000)
    alarm.manualStart()
else:
    p1.on()
    print('normal boot, no alarm')
    server.start()
