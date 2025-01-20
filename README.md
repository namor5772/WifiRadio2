# Internet Radio

Here we describe the design, construction, programming and operation of an internet radio with a minimal one button interface based on a Raspberry Pi.

There are 7 available radio stations. One scrolls through them by successively pressing the tactile switch. The station number selected is diplayed in binary by three red 5mm LEDs. When all three LEDs are off then no station is playing (number 0). When the radio is powered off (by removing power to the Raspberry Pi) the currently streaming station is saved so that when the radio is powered on later that station resumes streaming.

## Physical design

The TinyCad design file [WifiRadio2.dsn](WifiRadio2.dsn) for the interface circuitry is displayed below:
![WifiRadio2.net](WifiRadio2_dsn.png)

The resulting VeeCad file [WifiRadio2.per](WifiRadio2.per) is displayed below:

It is obtained from the Netlist file [WifiRadio2.net](WifiRadio2.net) generated from WifiRadio2.dsn (displayed above).
![WifiRadio2.per](WifiRadio2_per.png)

This is what the completed interface board looks like:
![interfaceboard image1](interfaceboard_image1.png)
Note that the LEDs are offset from the circuit board by 5mm using an appropriate piece of balsawood.
![interfaceboard image2](interfaceboard_image2.png)

## Enclosure

The interface circuit is placed in a custom 3D printed enclosure which is secured on top of the case that houses the Raspberry Pi. 5 wires connect the interface circuit to the Raspberry Pi. This is the internet radio to which stereo USB powered 3.5m audio speakers must be attached (to the underlying Raspberry Pi).

![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)
The case was designed using Blender.

The top of the case is in [WifiRadio2_BoxTop.blend](WifiRadio2_BoxTop.blend), while the bottom is in [WifiRadio2_BoxBottom.blend](WifiRadio2_BoxBottom.blend). To view or edit these files open them with the Blender 4.3 App in Windows 11.

To be able to 3D print the enclosure these files must be exported from the Blender App as [WifiRadio2_BoxTop.stl](WifiRadio2_BoxTop.stl) and [WifiRadio2_BoxBottom.stl](WifiRadio2_BoxBottom.stl) respectively.

Finally these *.stl files must be opened into the Crealty Print 6.0 Windows 11 App which creates the [WifiRadio2_BoxTop.3mf](WifiRadio2_BoxTop.3mf) and [WifiRadio2_BoxBottom.3mf](WifiRadio2_BoxBottom.3mfl) respectively. These contain the type of printer needed and other details of the print and are the basis for creating (by File => Export => Export Gcode...) the *.gcode files [WifiRadio2_BoxTop.gcode](WifiRadio2_BoxTop.gcode) and [WifiRadio2_BoxBottom.gcode](WifiRadio2_BoxBottom.gcode) respectively. These are the actual files used by the 3D Printer to do the actual printing! The files saved here are for the Crealty Ender-3 V3 SE printer with default setting for Hyper PLA.

If you have a different 3D printer you can still use the *.stl files but you will have to generate the *.gcode files yourself.



## Software

The radio is implemented in software by a python script [Radio5.py](Radio5.py) that auto starts through the Python IDLE shell when the the GUI becomes active. The audio streaming uses cvlc. A valid wifi connection is assumed to be available and automatically enabled when the Raspberry Pi is powered on.

```python
import subprocess
import time
import RPi.GPIO as GPIO
import os;    

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Create the full filepath to the saved radio station file
filename = 'savedRadioStation.txt'
filepath = os.path.join(script_directory, filename)
print(f'The file {filepath} stores the last streamed station number.')

# Use BCM GPIO numbering 
GPIO.setmode(GPIO.BCM)

# Define Raspberry Pi pins that go to the interface circuit board
button_pin = 26
led0_pin = 19
led1_pin = 13
led2_pin = 6

# Setup the pins
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)
GPIO.setup(led0_pin, GPIO.OUT)
GPIO.setup(led1_pin, GPIO.OUT)
GPIO.setup(led2_pin, GPIO.OUT)

# setup the leds to be initially all off
GPIO.output(led0_pin,GPIO.LOW)
GPIO.output(led1_pin,GPIO.LOW)
GPIO.output(led2_pin,GPIO.LOW)

# 2D array of radio station information in [short name, long name, url] format
aStation = [
    ["2LRW","ABC Radio Sydney","https://live-radio01.mediahubaustralia.com/2LRW/mp3/"],
    ["5LRW","ABC Radio National","https://live-radio01.mediahubaustralia.com/2RNW/mp3/"],
    ["PBW","ABC NewsRadio","https://live-radio01.mediahubaustralia.com/PBW/mp3/"],
    ["2FMW","ABC Classic Sydney","https://live-radio01.mediahubaustralia.com/2FMW/mp3/"],
    ["FM2W","ABC Classic 2","https://live-radio01.mediahubaustralia.com/FM2W/mp3/"],
    ["WSFM","GOLD 101.7","https://playerservices.streamtheworld.com/api/livestream-redirect/ARN_WSFM.mp3"],
    ["SMOOTH953","Smooth FM Sydney 95.3","https://playerservices.streamtheworld.com/api/livestream-redirect/SMOOTH953.mp3"]
]

# some utility global variables
vlc_path = "/usr/bin/cvlc" # full path to cvlc
Running = False # flag True if radio station is streaming
nStation = 0 # station number (0 is the "no radio streaming" station)
startup = True # True when radio initially powered up 

print("Radio stream interface")

while True:

    if ((GPIO.input(button_pin) == GPIO.LOW) or (startup)):
        time.sleep(0.2) # pathetic debouncing code

        if (startup):
            # load saved station number from file when radio powered up
            try:
                with open(filepath, 'r') as file:
                    nStation = int(file.read())
            except FileNotFoundError:
                print(f'Error: The file {filepath} does not exist.')
                nStation = 0
        else:
            # increment station number modulo 8 when button pressed
            if nStation == 7:
                nStation = 0
            else:
                nStation = nStation +1

            # save station number to file (if radio powered off when playing this station)
            with open(filepath, 'w') as file:
                file.write(str(nStation))

        # display the station number in binary
        bit0 = (nStation >> 0) & 1 # LSB
        bit1 = (nStation >> 1) & 1 # middle bit
        bit2 = (nStation >> 2) & 1 # MSB
        GPIO.output(led0_pin,bit0)
        GPIO.output(led1_pin,bit1)
        GPIO.output(led2_pin,bit2)
        print("Button pressed, Station: ",nStation)    

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
            if (not startup):
                # need to terminate current process, before starting new one
                process.terminate()
                
            process = subprocess.Popen([vlc_path, stream_url])
            Running = True
            print("Started streaming radio station: " + stream_longName)

        startup = False   

```
## Parts List

    EXPAND THE EXPLANATION OF THE PRECISE RASPBERRY PI INSTALLED SOFTWARE AND SETUP 

ENJOY!

