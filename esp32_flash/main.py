from umqtt.simple import MQTTClient
from machine import Pin, I2C, Timer
from bme280 import BME280
import json
import gc
import time
import network

SERVER = "192.168.50.2"
CLIENT_ID = "ESP32_bme280"
TOPIC = b"homeassistant/lolin/bme280"
USER = "mqtt"
PASS = "hassmqttusr"

def main(timer_id=None):
    led = Pin(5,Pin.OUT)
    i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)
    bme = BME280(i2c = i2c)
    mqtt = MQTTClient(CLIENT_ID,SERVER,1883,USER,PASS)
    try:
        mqtt.connect()
        js = json.dumps({
            "temperature": bme.temperature[:-1],
            "humidity": bme.humidity[:-1],
            "pressure": bme.pressure[:-3]
                })
        led.off()
        print(timer_id, js)
        mqtt.publish(TOPIC, js)
        led.on()
    except Exception as ex:
        print(ex)
    finally:
        mqtt.disconnect()
        gc.collect()

try:
    print("Starting...10sec periodic timer")
    tim = Timer(1)
    tim.init(period=10000, mode=Timer.PERIODIC,
                callback=lambda t:main('10_sec_timer'))
    while True:
        pass
except KeyboardInterrupt as ex:
    tim.deinit()
    gc.collect()
    print("Timer stopped")
    print(ex)
