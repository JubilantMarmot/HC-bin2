import machine
import math

from dht import DHT22
dht = DHT22(machine.Pin(22)) 

def read_temperature():
    dht.measure()
    temp = dht.temperature()
    hum = dht.humidity()

    return temp, hum