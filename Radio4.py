import subprocess
print(subprocess.__file__)
import time

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


# Replace with your radio station's streaming URL
#stream_url = 'https://live-radio01.mediahubaustralia.com/2LRW/mp3/'
#stream_url = 'https://live-radio01.mediahubaustralia.com/2FMW/mp3/'
#stream_url = 'https://playerservices.streamtheworld.com/api/livestream-redirect/ARN_WSFM.mp3'
#stream_url = 'https://playerservices.streamtheworld.com/api/livestream-redirect/SMOOTH953.mp3'
#vlc_path = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
vlc_path = "cvlc"

print("Radio stream interface")
print("Enter anything to scroll down one station. 'e' to stop program")

Running = False
nStation = 0

while True:
    user_input = input("Scroll one down through stations").strip().lower()

    if user_input == 'e':
        if Running:
            process.kill()
        print("Exiting...")
        break

    if nStation == 7:
        nStation = 0
    else:
        nStation = nStation +1

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



