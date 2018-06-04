from machine import Pin
from servo import servo

PIN_WHEEL_LEFT = 12
PIN_WHEEL_RIGHT = 14

wheel_left = servo(Pin(PIN_WHEEL_LEFT))
wheel_right = servo(Pin(PIN_WHEEL_RIGHT))

wheel_left.write_angle(100)