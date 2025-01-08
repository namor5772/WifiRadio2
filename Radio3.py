import os
import subprocess
import threading
import socket
import time

socket_path = '/tmp/vlc.sock'

# Remove existing socket file if it exists
if os.path.exists(socket_path):
    os.remove(socket_path)

def play_stream(stream_url):
    subprocess.call([
        'cvlc', '--quiet',
        '--extraintf', 'rc',
        '--rc-unix', socket_path,
        stream_url
    ])

def send_command(command):
    try:
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
            sock.connect(socket_path)
            sock.sendall((command + '\n').encode('utf-8'))
    except Exception as e:
        print(f"Error sending command '{command}': {e}")

# Replace with your actual stream URL
stream_url = 'http://live-radio01.mediahubaustralia.com/2LRW/aac/'

# Start VLC in a separate thread
player_thread = threading.Thread(target=play_stream, args=(stream_url,))
player_thread.daemon = True
player_thread.start()

time.sleep(2)  # Give VLC time to start

print("Streaming started. Enter 'p' to pause/resume, 's' to stop, 'q' to quit.")

try:
    while True:
        command = input("Command (p/s/q): ").strip().lower()
        if command == 'p':
            send_command('pause')
            print("Playback toggled.")
        elif command == 's':
            send_command('stop')
            print("Playback stopped.")
        elif command == 'q':
            send_command('quit')
            print("Exiting...")
            break
        else:
            print("Invalid command.")
except KeyboardInterrupt:
    print("\nInterrupted by user.")
    send_command('quit')
finally:
    player_thread.join()
    if os.path.exists(socket_path):
        os.remove(socket_path)
