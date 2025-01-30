# Internet Radio

Here we describe the design, construction, programming and operation of an internet radio with a minimal one button interface based on a Raspberry Pi.

There are 7 available radio stations. One scrolls through them by successively pressing the tactile switch. The station number selected is diplayed in binary by three red 5mm LEDs. When all three LEDs are off then no station is playing (number 0). When the radio is powered off (by removing power to the Raspberry Pi) the currently streaming station is saved so that when the radio is powered on later that station resumes streaming.

## Physical design

The TinyCad design file [WifiRadio2.dsn](Hardware/WifiRadio2.dsn) for the interface circuitry is displayed below:
![WifiRadio2.net](Images/WifiRadio2_dsn.png)

The resulting VeeCad file [WifiRadio2.per](Hardware/WifiRadio2.per) is displayed below:

It is obtained from the Netlist file [WifiRadio2.net](Hardware/WifiRadio2.net) generated from WifiRadio2.dsn (displayed above).
![WifiRadio2.per](Images/WifiRadio2_per.png)

This is what the completed interface board looks like:
![interfaceboard image1](Images/interfaceboard_image1.png)
Note that the LEDs are offset from the circuit board by 5mm using an appropriate piece of balsawood.
![interfaceboard image2](Images/interfaceboard_image2.png)

## Enclosure

The interface circuit is placed in a custom 3D printed enclosure which is secured on top of the case that houses the Raspberry Pi. 5 wires connect the interface circuit to the Raspberry Pi. This is the internet radio to which stereo USB powered 3.5m audio speakers must be attached (to the underlying Raspberry Pi).

![alt text](Images/image.png)
![alt text](Images/image-1.png)
![alt text](Images/image-2.png)
![alt text](Images/image-3.png)
The case for the interface circuit was designed using Blender.

The top of the case is in [WifiRadio2_BoxTop.blend](Hardware/WifiRadio2_BoxTop.blend), while the bottom is in [WifiRadio2_BoxBottom.blend](Hardware/WifiRadio2_BoxBottom.blend). To view or edit these files open them with the Blender 4.3 App in Windows 11.

To be able to 3D print the enclosure these files must be exported from the Blender App as [WifiRadio2_BoxTop.stl](Hardware/WifiRadio2_BoxTop.stl) and [WifiRadio2_BoxBottom.stl](Hardware/WifiRadio2_BoxBottom.stl) respectively.

Finally these *.stl files must be opened into the Crealty Print 6.0 Windows 11 App which creates the [WifiRadio2_BoxTop.3mf](Hardware/WifiRadio2_BoxTop.3mf) and [WifiRadio2_BoxBottom.3mf](Hardware/WifiRadio2_BoxBottom.3mfl) respectively. These contain the type of printer needed and other details of the print and are the basis for creating (by File => Export => Export Gcode...) the *.gcode files [WifiRadio2_BoxTop.gcode](Hardware/WifiRadio2_BoxTop.gcode) and [WifiRadio2_BoxBottom.gcode](Hardware/WifiRadio2_BoxBottom.gcode) respectively. These are the actual files used by the 3D Printer to do the actual printing! The files saved here are for the Crealty Ender-3 V3 SE printer with default setting for Hyper PLA.

If you have a different 3D printer you can still use the *.stl files but you will have to generate the *.gcode files yourself.

## Raspberry Pi setup

I have used a Raspberry Pi 2 Model B V1.1 2014, running Raspberry Pi OS (Legacy) on a 8Gb Micro SD HCI card (which you will have to image). It is configured to Boot To Desktop with Auto login, with only the Remote GPIO enabled. Since it does not have inbuilt wifi you will need a wifi dongle. Also USB powered 3.5m stereo audio speakers need to be attached. All this powered with appropreate power adaptor and cable
***COMPLETE***

 1. On your Windows 11 PC (and until further notice) format your SD Card
 2. Download the Raspberry Pi OS (Legacy) image file https://downloads.raspberrypi.com/raspios_oldstable_armhf/images/raspios_oldstable_armhf-2024-10-28/2024-10-22-raspios-bullseye-armhf.img.xz from the official Raspberry Pi website https://www.raspberrypi.com/.
 3. Extract it to a newly created directory. In my case C:\Users\\{username}\OneDrive\RaspberryPi\2024-10-22-raspios-bullseye-armhf.img\ which contains the actual image file [2024-10-22-raspios-bullseye-armhf.img](Software/2024-10-22-raspios-bullseye-armhf.img)
 4. Install the Raspberry Pi Imager https://downloads.raspberrypi.org/imager/imager_latest.exe from the official Raspberry Pi website
5. Run Imager for the above:
    1. set hostname: rpi,  username: {username},  password: {password}
    2. setup wifi with available SSID and known password
6. Once completed image remove SD card from Windows 11 PC and put into your Raspberry Pi.
7. Power up/reboot Raspberry Pi and assuming you are using a mouse, keyboard and HDMI monitor. In the Raspberry Pi Configuration:
    1. In System tab: set Boot To desktop, Auto Login On.
    2. In Interfaces: only set Remote GPIO to on.
    3. Wireless LAN Country: AU Australia (or as appropriate)
8. Now on the rebooted running Raspberry Pi which should have auto logged into a GUI and have Wifi available. In a terminal windows:
    ```terminal
    {username}@rpi:~ $ sudo apt update
    {username}@rpi:~ $ sudo apt install python3 idle3
    {username}@rpi:~ $ sudo apt install vlc
    ```
    This will install the Python, Idle and vlc (and cvlc) applications which will reside in /usr/bin/
9. Create an autostart directory /home/{username}//.config/autostart and using nano create a file called autovlc.desktop in that directory, with the foillowing contents:    
    ```terminal
    [Desktop Entry]
    Type=Application
    Exec=/usr/bin/idle -r /home/{username}/Github/WifiRadio2/Radio5.py
    ```
10. Create a directory for the python script: /home/{username}/Github/WifiRadio2 and copy the python script Radio5.py into that directory (eg. using a USB memory stick with Radio5.py on it loaded from here).

    This way of running the script via autostart in the GUI is because I tried to run it after boot in the Command Line Interface (CLI), however I could not make this work due to some privilage issues which made vlc unable to execute. This would have been more efficient and elegant but I just wanted to make it work.

11. Finally in the GUI set the volume to 100% using the slider. This will persist over reboots and enable volume to be controlled over the full range using just the speakers control.
12. if you move the location of this internet radio you will need to setup another wifi connection. This involves identifying an SSID with a strong sigmal and inputting its password. This will the automatically connect to wifi on reboot if you are in range.

## Software

The radio is implemented in software by a python script [Radio5.py](Radio5.py) that auto starts through the Python IDLE shell when the the GUI becomes active. The audio streaming uses cvlc. A valid wifi connection is assumed to be available and automatically enabled when the Raspberry Pi is powered on.

```python
# all part of the Python standard libraries, with RPI.GPIO pre installed as part of the Raspian os
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

# Define the 4 Raspberry Pi pins that go to the interface circuit board
# Ground is not included
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
# clearly this can be varied if you wish to listen to different 7 stations
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
vlc_path = "/usr/bin/cvlc" # full path to cvlc, it is installed together with vlc
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
## List of parts

Pricing and availability as of 26-Jan-2025. Total cost is $250.57, but clearly some of the items will be usable in many other projects or you will already have them. The pro rata cost is __$209.11__

You will also need a soldering iron and solder, some two sided tape for attaching the circuit enclosure on top of the Raspberry Pi case as well as a printer to print the station legend for taping/sticking to the top of the enclosure. 

| Qty | Product | Description | AUD Cost | Comment | Designator |
| --- | --- | --- | --- | --- | --- |
| 1 | [RPI4-MODBP-4GB](https://au.element14.com/raspberry-pi/rpi4-modbp-4gb/raspberry-pi-4-model-b-4gb/dp/3051887?CMP=KNC-MAU-GEN-SHOPPING) | SBC, [Raspberry Pi4 B 4GB](Images/RPI4B.png), BCM2711, ARM Cortex-A72, 4GB RAM, MicroSD, Linux, Wifi, 2x micro HDMI | $92.65 | The brains of this project with this [datasheet](Hardware/4170044.pdf)  | connected via J1 |
| 1 | [XC4992](https://jaycar.com.au/p/XC4992) | 32GB Class 10 microSDHC [Card](Images/Card.png) | $12.95 | For Raspberry Pi OS and storage | |
| 1 | [PH-102475](https://raspberry.piaustralia.com.au/products/highpi-raspberry-pi-4-model-b-case) | HighPi Raspberry Pi 4 Model B [Case](Images/Case.png) | $32.12 | could use other cases | |
| 1 | [HP9544](https://jaycar.com.au/p/HP9544) | PC Boards Vero Type [Strip](Images/Strip.png) - 95mm x 305mm | $15.50 | Contains the circuit | $4.00 cost used|
| 3 | [ZD0150](https://jaycar.com.au/p/ZD0150) | Red 5mm [LED](Images/LED.png) 8mcd Round Diffused | $1.20 | indicate status in binary | D0, D1, D2 |
| 1 | [SP0720](https://jaycar.com.au/p/SP0720) | Red Snap Action Keyboard [Switch](Images/Switch.png) - PCB Mount | $1.45 | The only input item | SW1 |
| 1 | [RR0556](https://jaycar.com.au/p/RR0556) | 220 Ohm 0.5 Watt Metal Film [Resistors](Images/Resistor.png) - Pack of 8 (only need 3) | $0.85 | Current limiting for LEDs | R0, R1, R2 - $0.32 cost used|
| 1 | [HM3422](https://jaycar.com.au/p/HM3422) | 2 Pin 0.1in 90 Degree Locking [Header](Images/Header2.png) - 2.54mm Pitch - Single | $0.30 | connector to RPi | part of J1 |
| 1 | [HM3423](https://jaycar.com.au/p/HM3423) | 3 Pin 0.1in 90 Degree Locking [Header](Images/Header3.png) - 2.54mm Pitch - Single | $0.40 | connector to RPi | part of J1 |
| 1 | [WW4030](https://jaycar.com.au/p/WW4030) | Tinned Copper [Wire](Images/Wire.png) - 100 gram Roll | $19.95 | for wiring up above Vero board | $0.80 cost used|
| 1 | [WC6026](https://jaycar.com.au/p/WC6026) | 150mm Socket to Socket Jumper [Leads](Images/Leads.png) - 40 Piece | $11.75 | 5 wires to connect Vero Board to Raspberry Pi | connects to J1 - $1.47 cost used|
| 1 | [XC5191](https://jaycar.com.au/p/XC5191) | USB Powered PC [Speakers](Images/Speakers.png) | $19.75 | Any if USB powered & 3.5mm input | |
| 1 | [MP3449](https://jaycar.com.au/p/MP3449) | Mains USB Mini Power [Adaptor](Images/Adaptor.png) - 2.4A | $26.95 | to Power Raspberry Pi | |
| 1 | [WC7900](https://jaycar.com.au/p/WC7900) | USB Type-C to USB 2.0 A Male [Cable](Images/Cable.png) 1.8m | $14.75 | to Power Raspberry Pi | |