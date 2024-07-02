# ITP Camp Camera Project

![Gui in the camp holding up a peace sign, in the first image taken by the caera](firstimage.jpg)

## Demo

```
python camera.py
```

Enables taking photos by pressing the button attached to pin 10.

To see the images, host a simple HTTP server with

```
python -m http.server -d camimages
```

then navigate to `http://raspberrypi.local:8000`.
