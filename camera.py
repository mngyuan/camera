from picamera2 import Picamera2
from gpiozero import Button
from datetime import datetime
from signal import pause
import subprocess

def take_photo():
    picam2.capture_file(f'/home/pi/picam2img/{datetime.now():%Y-%m-%d-%H-%M-%S}.jpg')
    print(f'Saved to /home/pi/picam2img/{datetime.now():%Y-%m-%d-%H-%M-%S}.jpg')

button = Button("BOARD10", pull_up=False)

button.when_pressed = take_photo

picam2 = Picamera2()
preview_config = picam2.create_still_configuration()

# Get the camera configuration
config = picam2.create_still_configuration()
controls = config["controls"]

# Disable AE and AWB
controls["AeEnable"] = False
controls["AwbEnable"] = False

# Set manual controls (if needed)
controls["ExposureTime"] = 10000  # in microseconds
controls["AnalogueGain"] = 1.0
controls["ColourGains"] = (1.5, 1.2)  # Red, Blue gains

# Apply the configuration
picam2.configure(config)
picam2.start()

pause()
