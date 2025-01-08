import subprocess
print(subprocess.__file__)
import time

# 2D array of radio station information in [short name, long name, url] format

# station = [

            


# Replace with your radio station's streaming URL
stream_url = 'http://live-radio01.mediahubaustralia.com/2LRW/aac/'

# Start streaming using cvlc
#process = subprocess.Popen(['cvlc', stream_url])

print("Radio stream interface")
print("Enter 's' to start streaming, 'q' to quit streaming. 'e' to stop program")

Running = False

while True:
    user_input = input("Command (s/q/e): ").strip().lower()
    if user_input == 's':
        if not Running:
            process = subprocess.Popen(["cvlc", stream_url])
            Running = True
            print("Started streaming radio station")
        else:
            print("Cannot restart streaming if it as already streaming")
    elif user_input == 'q':
        if Running:
            process.terminate()
            Running = False
            print("stopped streaming radio station")
        else:
            print("nothing to stop")
    elif user_input == 'e':
        if Running:
            process.kill()
            print("Exiting...")
        break
    else:
        print("Invalid command. Please enter 's', 'q', or 'e'.")
