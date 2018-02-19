import time
from air_analyser import air_analyser
from mqtt_client import mqtt_client

client = mqtt_client('192.168.0.235')
air = air_analyser()

while True:
    temp,hum = air.get_measurement()
    client.send_msg('temperature',temp)
    client.send_msg('humidity',hum)
    time.sleep(10)