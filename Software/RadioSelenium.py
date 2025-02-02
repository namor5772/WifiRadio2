# all part of the Python standard libraries, with RPI.GPIO pre installed as part of the Raspian os
import subprocess

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Path to Geckodriver executable
geckodriver_path = 'C:\\Users\\roman\\OneDrive\\MyImportant\\geckodriver.exe'  # Adjust this path

# Set up Firefox options
browser = webdriver.Firefox()
browser.get("https://www.abc.net.au/listen/live/classic")
body_element = browser.find_element(By.TAG_NAME, 'body')
body_element.send_keys(Keys.TAB)
body_element.send_keys(Keys.TAB)
body_element.send_keys(Keys.TAB)
body_element.send_keys(Keys.TAB)
body_element.send_keys(Keys.TAB)
body_element.send_keys(Keys.TAB)
body_element.send_keys(Keys.TAB)
body_element.send_keys(Keys.TAB)
body_element.send_keys(Keys.ENTER)
time.sleep(5)
browser.get("https://www.abc.net.au/listen/live/classic")



#options.headless = False  # Set to True to run headless (without GUI)

# Start Firefox browser with Geckodriver
#service = Service(geckodriver_path)
#driver = webdriver.Firefox(service=service, options=options)

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
vlc_path = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'
#vlc_path = "/usr/bin/cvlc" # full path to cvlc
Running = False # flag True if radio station is streaming
nStation = 0 # station number (0 is the "no radio streaming" station)
startup = True # True when radio initially powered up 

print("Radio stream interface")

nStation = 1
stream_url = aStation[nStation-1][2]
stream_longName = aStation[nStation-1][1]
process = subprocess.Popen([vlc_path, stream_url])
print("Started streaming radio station: " + stream_longName)


while True:
    startup = False    

