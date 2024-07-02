from gpiozero import Button
from datetime import datetime
from signal import pause
import subprocess

def say_hello():
    subprocess.run(['rpicam-still', '--raw', '--output', f'/home/pi/camimages/{datetime.now():%Y-%m-%d-%H-%M-%S}.jpg'])
    print(f'Saved to /home/pi/{datetime.now():%Y-%m-%d-%H-%M-%S}.jpg')

button = Button("BOARD10", pull_up=False)

button.when_pressed = say_hello

pause()

