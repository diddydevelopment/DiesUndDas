from umqtt.simple import MQTTClient

class mqtt_client:
    def __init__(self,ip,port=1883):
        self._conn = MQTTClient("client",ip,port)
        self._conn.connect()

    def send_msg(self,channel,msg):
        self._conn.publish(channel,str(msg))


# client.set_callback(setMotor)
# client.wait_msg()
