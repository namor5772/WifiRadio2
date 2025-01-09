import subprocess
import time
import RPi.GPIO as GPIO

# Use BCM GPIO numbering 
GPIO.setmode(GPIO.BCM)

# Define pins that goes to the circuit
button_pin = 17
led0_pin = 26
led1_pin = 19
led2_pin = 13

# Setup the pins
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)
GPIO.setup(led0_pin, GPIO.OUT)
GPIO.setup(led1_pin, GPIO.OUT)
GPIO.setup(led2_pin, GPIO.OUT)

# setpup the leds
GPIO.output(led0_pin,GPIO.LOW)
GPIO.output(led1_pin,GPIO.LOW)
GPIO.output(led2_pin,GPIO.LOW)

# 2D array of radio station information in [short name, long name, url] format
aStation = [
    ["PBW","ABC NewsRadio","https://live-radio01.mediahubaustralia.com/PBW/mp3/"],
    ["2LRW","ABC Radio Sydney","https://live-radio01.mediahubaustralia.com/2LRW/mp3/"],
    ["5LRW","ABC Radio Adelaide","https://live-radio01.mediahubaustralia.com/5LRW/mp3/"],
    ["FM2W","ABC Classic 2","https://live-radio01.mediahubaustralia.com/FM2W/mp3/"],
    ["2FMW","ABC Classic Sydney","https://live-radio01.mediahubaustralia.com/2FMW/mp3/"],
    ["WSFM","GOLD 101.7","https://playerservices.streamtheworld.com/api/livestream-redirect/ARN_WSFM.mp3"],
    ["SMOOTH953","Smooth FM Sydney 95.3","https://playerservices.streamtheworld.com/api/livestream-redirect/SMOOTH953.mp3"]
]

vlc_path = "/usr/bin/cvlc"

print("Radio stream interface")

Running = False
nStation = 0

while True:

    if GPIO.input(button_pin) == GPIO.LOW:
        time.sleep(0.2)    
        
        if nStation == 7:
            nStation = 0
        else:
            nStation = nStation +1
        print("Button pressed, Station: ",nStation)    

        # display the station number in binary
        bit0 = (nStation >> 0) & 1 # LSB
        bit1 = (nStation >> 1) & 1 # middle bit
        bit2 = (nStation >> 2) & 1 # MSB
        GPIO.output(led0_pin,bit0)
        GPIO.output(led1_pin,bit1)
        GPIO.output(led2_pin,bit2)
        

        if nStation > 0:
            stream_url = aStation[nStation-1][2]
            stream_longName = aStation[nStation-1][1]

        if nStation == 0:
            if Running:    
                process.terminate()
            Running = False
            print("No streaming")

        elif nStation == 1:
            # started new process, but no need to terminate previous one since already terminated
            process = subprocess.Popen([vlc_path, stream_url])
            Running = True
            print("Started streaming radio station: " + stream_longName)

        else:
            # need to terminate current process, before starting new one
            process.terminate()
            process = subprocess.Popen([vlc_path, stream_url])
            Running = True
            print("Started streaming radio station: " + stream_longName)



