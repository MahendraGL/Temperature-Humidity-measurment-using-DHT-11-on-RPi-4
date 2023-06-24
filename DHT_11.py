import RPi.GPIO as GPIO
import time
import dht11
GPIO.setmode(GPIO.BOARD)
myDHT=dht11.DHT11(pin=40)

try:
    while True:
        output=myDHT.read()
        if output.is_valid():
            print("Tempearture is: ",output.temperature,"Degrees")
            print("Humidity is :",output.humidity,"%")
        time.sleep(.5)
    
except KeyboardInterrupt:
    GPIO.cleanup()
    print("DONE")