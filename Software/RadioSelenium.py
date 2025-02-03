import subprocess
import inspect

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to Geckodriver executable
#geckodriver_path = 'C:\\Users\\roman\\OneDrive\\MyImportant\\geckodriver.exe'  # Adjust this path

# Create an instance of FirefoxOptions
firefox_options = Options()

# Example: Set headless mode (runs browser in background)
firefox_options.add_argument("-headless")  # Ensure this argument is correct

# Set up the Firefox driver with options
browser = webdriver.Firefox(options=firefox_options)

# Set up Firefox options
#browser = webdriver.Firefox()



# START ***** Functions that stream radio stations *****

def Keys1(be):
    print(inspect.stack()[1].function)
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.ENTER)
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.ENTER)
    be.send_keys(Keys.SHIFT,Keys.TAB)
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.TAB)

def Keys2(be,Num):
    print(inspect.stack()[1].function)
    for _ in range(Num):
        be.send_keys(Keys.TAB)
    be.send_keys(Keys.ENTER)
    
def Keys3(be,Num):
    print(inspect.stack()[1].function)
    for _ in range(Num):
        be.send_keys(Keys.TAB)
    be.send_keys(Keys.ENTER)
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.TAB)

def Keys4(br,sPath):
    print(inspect.stack()[1].function)
    br.refresh()
    br.get(sPath)
    time.sleep(3)
    window_size = br.get_window_size()
    #print(f"Window size: width = {window_size['width']}, height = {window_size['height']}")
    actions = ActionChains(br)
    actions.move_by_offset(301, 256).click().perform()
    time.sleep(10)

    

def ABC_Radio_SYDNEY():
    browser.refresh()
    browser.get("https://www.abc.net.au/listen/live/sydney")
    time.sleep(3)
    body_element = browser.find_element(By.TAG_NAME, 'body')
    Keys1(body_element)

def ABC_Radio_National_LIVE():
    browser.refresh()
    browser.get("https://www.abc.net.au/listen/live/radionational")
    time.sleep(3)
    body_element = browser.find_element(By.TAG_NAME, 'body')
    Keys2(body_element,6)

def ABC_NewsRadio():
    browser.refresh()
    browser.get("https://www.abc.net.au/listen/live/news")
    time.sleep(3)
    body_element = browser.find_element(By.TAG_NAME, 'body')
    Keys1(body_element)

def ABC_Classic_LIVE():
    browser.refresh()
    browser.get("https://www.abc.net.au/listen/live/classic")
    time.sleep(3)
    body_element = browser.find_element(By.TAG_NAME, 'body')
    Keys2(body_element,8)

def ABC_Classic2():
    browser.refresh()
    browser.get("https://www.abc.net.au/listen/live/classic2")
    time.sleep(3)
    body_element = browser.find_element(By.TAG_NAME, 'body')
    Keys2(body_element,7)

def ABC_Jazz():
    browser.refresh()
    browser.get("https://www.abc.net.au/listen/live/jazz")
    time.sleep(3)
    body_element = browser.find_element(By.TAG_NAME, 'body')
    Keys2(body_element,7)

def ABC_triple_j_LIVE():
    browser.refresh()
    browser.get("https://www.abc.net.au/listen/live/triplej")
    time.sleep(3)
    body_element = browser.find_element(By.TAG_NAME, 'body')
    Keys2(body_element,8)

def ABC_Double_j_LIVE():
    browser.refresh()
    browser.get("https://www.abc.net.au/listen/live/doublej")
    time.sleep(3)
    body_element = browser.find_element(By.TAG_NAME, 'body')
    Keys2(body_element,8)

def ABC_triple_j_Unearthed():
    browser.refresh()
    browser.get("https://www.abc.net.au/triplej/live/unearthed")
    time.sleep(3)
    body_element = browser.find_element(By.TAG_NAME, 'body')
    Keys2(body_element,7)

def ABC_triple_j_Hottest():
    browser.refresh()
    browser.get("https://www.abc.net.au/triplej/live/triplejhottest")
    time.sleep(3)
    body_element = browser.find_element(By.TAG_NAME, 'body')
    Keys2(body_element,7)

def ABC_Country():
    browser.refresh()
    browser.get("https://www.abc.net.au/listen/live/country#content")
    time.sleep(3)
    body_element = browser.find_element(By.TAG_NAME, 'body')
    Keys3(body_element,3)

def ABC_Radio_AUSTRALIA():
    browser.refresh()
    browser.get("https://www.abc.net.au/pacific/live")
    time.sleep(3)
    body_element = browser.find_element(By.TAG_NAME, 'body')
    Keys3(body_element,14)
    time.sleep(3)


  
def KIIS1065():
    Keys4(browser,"https://www.iheart.com/live/kiis-1065-6185/")

def GOLD1017():
    Keys4(browser,"https://www.iheart.com/live/gold1017-6186/")

def CADA():
    Keys4(browser,"https://www.iheart.com/live/cada-6179/")

def iHeartCountry_Australia():
    Keys4(browser,"https://www.iheart.com/live/iheartcountry-australia-7222/")
    
def KIIS_90s():
    Keys4(browser,"https://www.iheart.com/live/kiis-90s-10069/")

def GOLD_80s():
    Keys4(browser,"https://www.iheart.com/live/gold-80s-10073/")

def iHeartRadio_Countdown_AUS():
    Keys4(browser,"https://www.iheart.com/live/iheartradio-countdown-aus-6902/")

def TikTok_Trending_on_iHeartRadio():
    Keys4(browser,"https://www.iheart.com/live/tiktok-trending-on-iheartradio-8876/")

def iHeartDance():
    Keys4(browser,"https://www.iheart.com/live/iheartdance-6941/")

def The_Bounce():
    Keys4(browser,"https://www.iheart.com/live/the-bounce-6327/")

def iHeartAustralia():
    Keys4(browser,"https://www.iheart.com/live/iheartaustralia-7050/")

def fbi_radio():
    Keys4(browser,"https://www.iheart.com/live/fbiradio-6311/")

def _2SER1073():
    Keys4(browser,"https://www.iheart.com/live/2ser-6324/")





# END ******* Functions that stream radio stations *****


        



# 2D array of radio station information in [short name, long name, url] format
# clearly this can be varied if you wish to listen to different 7 stations
aStation = [
    ["ABC Radio AUSTRALIA",ABC_Radio_AUSTRALIA],
    ["ABC Radio National LIVE",ABC_Radio_National_LIVE],
    ["PBW","ABC NewsRadio","https://live-radio01.mediahubaustralia.com/PBW/mp3/"],
    ["2FMW","ABC Classic Sydney","https://live-radio01.mediahubaustralia.com/2FMW/mp3/"],
    ["FM2W","ABC Classic 2","https://live-radio01.mediahubaustralia.com/FM2W/mp3/"],
    ["WSFM","GOLD 101.7","https://playerservices.streamtheworld.com/api/livestream-redirect/ARN_WSFM.mp3"],
    ["SMOOTH953","Smooth FM Sydney 95.3","https://playerservices.streamtheworld.com/api/livestream-redirect/SMOOTH953.mp3"]
]

print("Radio stream interface")

ABC_Radio_AUSTRALIA()
time.sleep(10)

ABC_Radio_National_LIVE()
time.sleep(10)

KIIS1065()
time.sleep(10)

GOLD1017()
time.sleep(10)

CADA()
time.sleep(10)

iHeartCountry_Australia()
time.sleep(10)

KIIS_90s()
time.sleep(10)

GOLD_80s()
time.sleep(10)

iHeartRadio_Countdown_AUS()
time.sleep(10)

TikTok_Trending_on_iHeartRadio()
time.sleep(10)

iHeartDance()
time.sleep(10)

The_Bounce()
time.sleep(10)

iHeartAustralia()
time.sleep(10)

fbi_radio()
time.sleep(10)

_2SER1073()
time.sleep(10)

ABC_Country()



while True:
    startup = False    

