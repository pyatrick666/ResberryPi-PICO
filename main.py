from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd
from DHT22 import DHT22
import utime
import time

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=100000)

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

dht22=DHT22(Pin(15,Pin.IN,Pin.PULL_UP))#sensor connected GPIO 15 pin 

while True:
    T, H = dht22.read()
    lcd.move_to(0,0)
    lcd.putstr("Temp :")
    lcd.move_to(7,0)
    lcd.putstr(str(T)+"C")
    
    lcd.move_to(0,1)
    lcd.putstr("Humi :")
    lcd.move_to(7,1)
    lcd.putstr(str(H))
    print(T,H)
    time.sleep_ms(500)

