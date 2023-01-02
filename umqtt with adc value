import machine
from machine import ADC
from time import sleep
from umqtt.simple import MQTTClient
import network

# Test reception e.g. with:
# mosquitto_sub -t foo_topic
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("moto", "suresh30065")

while not wlan.isconnected():
    print('.')
    sleep(1)
    pass

print(wlan.ifconfig())

adc = ADC(0)
sleep(0.1)


def message_callback(topic, msg):
    print(topic, msg)

def main(server="181.215.79.108"):
    c = MQTTClient("ESP8266-501","181.215.79.108",1883,"mqttadmin","627502")
    c.connect()
    c.set_callback(message_callback)
    c.subscribe(b"servermsg")
    
    while True:
        c.check_msg()
        ldr_val = adc.read()
        send_msg = str(ldr_val)
        sleep(.20)
        c.publish(b"ESP0106", send_msg)
        sleep(2)
    
    c.disconnect()

if __name__ == "__main__":
    main()
