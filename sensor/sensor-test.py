import logging
import signal
import time
from random import randint

from pyhap.accessory import Accessory
from pyhap.accessory_driver import AccessoryDriver
from pyhap.const import CATEGORY_SENSOR
from telegraf.client import TelegrafClient

logging.basicConfig(level=logging.INFO, format="[%(module)s] %(message)s")


class AM2302(Accessory):
    category = CATEGORY_SENSOR

    def __init__(self, *args, pin=4, **kwargs):
        super().__init__(*args, **kwargs)
        self.pin = pin

        serv_temp = self.add_preload_service('TemperatureSensor')
        serv_humidity = self.add_preload_service('HumiditySensor')

        self.char_temp = serv_temp.get_characteristic('CurrentTemperature')
        self.char_humidity = serv_humidity \
            .get_characteristic('CurrentRelativeHumidity')

        self.sensor = "AAA"

    def __getstate__(self):
        state = super().__getstate__()
        state['sensor'] = None
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.sensor = "AAA"

    @Accessory.run_at_interval(3)
    def run(self):
        # self.sensor.trigger()
        time.sleep(0.2)

        t = randint(16, 30)
        h = randint(0, 100)

        client.metric('AM2302', {'temperature': t, 'humidity': h}, tags={'room': 'bedroom'})

        self.char_temp.set_value(t)
        self.char_humidity.set_value(h)


if __name__ == "__main__":
    # Start
    client = TelegrafClient(host='0.0.0.0', port=8125)

    # Start the accessory on port 51826
    accessory_driver = AccessoryDriver(port=51826)
    climate_sensor = AM2302(accessory_driver, 'Temperature and Humidity Sensor')
    accessory_driver.add_accessory(accessory=climate_sensor)
    signal.signal(signal.SIGTERM, accessory_driver.signal_handler)

    accessory_driver.start()
