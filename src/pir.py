import wiringpi as pi
import time

PIR_PIN = 23

pi.wiringPiSetupGpio()
pi.pinMode( PIR_PIN, pi.INPUT )

while True:
    if ( pi.digitalRead( PIR_PIN ) == pi.HIGH ):
        print ("Someone is there.")
    else:
        print ("Nobody is there.")

    time.sleep(1)
