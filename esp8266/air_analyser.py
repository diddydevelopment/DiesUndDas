import machine
import dht

class air_analyser:
    def __init__(self,pin=2,sensor='dht11'):
        if sensor == 'dht11':
            self._d = dht.DHT11(machine.Pin(pin))
        elif sensor == 'dht22':
            self._d = dht.DHT22(machine.Pin(pin))
        else:
            raise NotImplementedError
    def get_measurement(self):
        self._d.measure()
        return self._d.temperature(),self._d.humidity()