import machine
from machine import Pin, I2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep

I2C_ADDR = 0x27

ldr = machine.ADC(0)

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266

devices = i2c.scan()

for device in devices:
    print(f'Found device on {hex(device)}')

lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
sleep(0.2)

while True:
    lcd.clear()
    lcd.putstr("SKARDUINO LABS")
    lcd.move_to(0,1) #x column ,y row
    temp = ldr.read()
    lcd.putstr(str(temp))
    sleep(2)
