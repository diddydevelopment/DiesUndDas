import machine

switch1 = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
switch2 = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_UP)
switch3 = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
	print(switch1.value(),switch2.value(),switch3.value())