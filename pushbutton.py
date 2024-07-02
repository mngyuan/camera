from gpiozero import Button

button = Button("BOARD10", pull_up=False)

while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")

