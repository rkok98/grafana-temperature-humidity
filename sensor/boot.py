import gc
import network
import esp

import config

esp.osdebug(None)
gc.collect()

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(config.ssid, config.password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())
