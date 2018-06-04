import pyb
from machine import Pin
buz_tim = pyb.Timer(3, freq=440)
buz_ch = buz_tim.channel(1, pyb.Timer.PWM, pin=Pin(2), pulse_width=0)
def play_tone(freq, msec):
    print('freq = {:6.1f} msec = {:6.1f}'.format(freq, msec))
    if freq > 0:
        buz_tim.freq(freq)
        buz_ch.pulse_width_percent(50)
    pyb.delay(int(msec * 0.9))
    buz_ch.pulse_width_percent(0)
    pyb.delay(int(msec * 0.1))
