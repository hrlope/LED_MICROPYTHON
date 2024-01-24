# Escribe tu código aquí :-)
#Do by Ricardo Moyano
import machine
import time

led_verde=machine.Pin(15,machine.Pin.OUT)

led_verde.on()
time.sleep_ms(1000)
led_verde.off()
time.sleep_ms(200)
led_verde.on()
time.sleep_ms(800)
led_verde.off()
