import machine
import dht
from umqttsimple import MQTTClient

import time

import config

sensor = dht.DHT22(machine.Pin(14))


def connect_and_subscribe():
    client = MQTTClient(config.client_id, config.mqtt_server)
    client.connect()
    print('Connected to %s MQTT broker, subscribed to %s topic' %
          (config.mqtt_server, config.topic_pub))
    return client


def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)
    machine.reset()


try:
    client = connect_and_subscribe()
except OSError as e:
    restart_and_reconnect()

last_message = 0

while True:
    try:
        if (time.time() - last_message) > 0.2:
            sensor.measure()
            temp = sensor.temperature()
            hum = sensor.humidity()

            msg = b'dht22 temperature=%d,humidity=%d' % (temp, hum)

            client.publish(config.topic_pub, msg)
            last_message = time.time()
            print(msg)
    except OSError as e:
        restart_and_reconnect()
