import subprocess
import threading
import socket
import time

def play_stream(stream_url, socket_path='/tmp/vlc.sock'):
    subprocess.call([
        'cvlc',
        '--quiet',
        '--extraintf', 'rc',
        '--rc-unix', socket_path,
        stream_url
    ])

def send_command(command, socket_path='/tmp/vlc.sock'):
    try:
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
            sock.connect(socket_path)
            sock.sendall((command + '\n').encode('utf-8'))
    except Exception as e:
        print(f"Error sending command '{command}': {e}")

# Replace with your radio stream URL
stream_url = 'http://live-radio01.mediahubaustralia.com/2LRW/aac/'

# Start VLC in a separate thread
player_thread = threading.Thread(target=play_stream, args=(stream_url,))
player_thread.daemon = True
player_thread.start()

# Allow some time for VLC to initialize
time.sleep(2)

print("Radio stream is playing.")
print("Enter 'p' to pause/resume, 's' to stop, or 'q' to quit.")

try:
    while True:
        user_input = input("Command (p/s/q): ").strip().lower()
        if user_input == 'p':
            send_command('pause')
            print("Playback toggled.")
        elif user_input == 's':
            send_command('stop')
            print("Playback stopped.")
        elif user_input == 'q':
            send_command('quit')
            print("Exiting...")
            break
        else:
            print("Invalid command. Please enter 'p', 's', or 'q'.")
except KeyboardInterrupt:
    print("\nInterrupted by user.")
    send_command('quit')
finally:
    player_thread.join()
