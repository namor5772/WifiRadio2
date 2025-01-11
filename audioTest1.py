import subprocess

vlc_path = "/usr/bin/cvlc"
stream_url = "https://live-radio01.mediahubaustralia.com/2LRW/mp3/"

print("Radio streaming")
process = subprocess.Popen([vlc_path, stream_url])
