# Climate sensor streaming with Homekit, Telegraf, InfluxDB and Grafana 

This project allows you to monitor and track the climate conditions of your room in real-time using a Raspberry PI and an ESP32 microcontroller. The project utilizes Docker to run the various services, including Homebridge and Telegraf, which act as an interface between the ESP32 and the InfluxDB database. The collected data is then visualized using Grafana, a powerful dashboard tool that enables you to analyze and understand your climate data.

```mermaid
sequenceDiagram
  Sensor (ESP32) ->> Mosquito MQTT broker: Publishes temperature and humidity data on topic: bedroom

  Telegraf ->> Mosquito MQTT broker: Subscribes to topic: bedroom
  Telegraf ->> InfluxDB: Sends temperature and humidity data
  Telegraf ->> Mosquito MQTT broker: Publishes temperature and humidity data on topic: telegraf/dht22

  Grafana ->> InfluxDB: Reads temperature and humidity
  Homebridge ->> Mosquito MQTT broker: Subscribes to topic: telegraf/dht22
```

## Sensor
- ESP32 with WiFi-module
- DHT22 
- MicroPython

### Build sensor
```bash
make setup_sensor
```

## Stack
- Mosquitto MQTT
- Telegraf
- InfluxDB
- Grafana
- Homebridge (optional)

### Start the stack with docker compose

```bash
$ docker-compose up
```
