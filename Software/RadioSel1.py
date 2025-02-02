import subprocess

def start_stream(stream_url):
    # Path to VLC executable
    vlc_path = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'
    
    # Start the VLC process with the stream URL
    subprocess.Popen([vlc_path, stream_url])

if __name__ == "__main__":
    stream_url = 'https://live-radio01.mediahubaustralia.com/2LRW/mp3/'  # Replace with the actual stream URL
    start_stream(stream_url)
