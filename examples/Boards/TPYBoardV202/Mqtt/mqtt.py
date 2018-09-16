from simple import MQTTClient
from machine import Pin
import machine
import micropython
#ѡ��G4����
g4 = Pin(4, Pin.OUT, value=0)
# MQTT��������ַ����Ϊ��183.230.40.39,����
SERVER = "183.230.40.39"
#�豸ID
CLIENT_ID = "9377500"
#����������
TOPIC = b"TurnipRobot"
#��ƷID
username='91025'
#��ƷAPIKey:
password='y7zd=7wNaObdfRYhxQn7D5jiDnI='
state = 0
def sub_cb(topic, msg):
    global state
    print((topic, msg))
    if msg == b"on":
            g4.value(1)
            state = 1
            print("1")
    elif msg == b"off":
            g4.value(0)
            state = 0
            print("0")
    elif msg == b"toggle":

            state = 1 - state
            g4.value(state)
           
def main(server=SERVER):
    #�˿ں�Ϊ��6002
    c = MQTTClient(CLIENT_ID, server,6002,username,password)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(TOPIC)
    print("Connected to %s, subscribed to %s topic" % (server, TOPIC))
    try:
        while 1:
            c.wait_msg()
    finally:
            c.disconnect()
