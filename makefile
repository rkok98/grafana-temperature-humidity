# Upload MicroPython files to ESP32
setup_sensor:
	ls ./sensor/*.py | xargs -n 1 ampy --port /dev/tty.usbserial-1450 put
