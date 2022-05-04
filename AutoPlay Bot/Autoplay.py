import time
import keyboard
from PIL import Image, ImageGrab
import winsound
frequency = 100  # Set Frequency To 2500 Hertz
duration = 80  # Set Duration To 1000 ms == 1 second

# Keybinds
key1 = 'a' # note 1
key2 = 's' # note 2
key3 = 'k' # note 3
key4 = 'l' # note 4

# System on/off
v1 = 0 # note 1
v2 = 0 # note 2
v3 = 0 # note 3
v4 = 0 # note 4

# Color notes
vc1 = (199, 144, 0) # note 1
vc2 = (199, 144, 0) # note 2
vc3 = (199, 144, 0) # note 3
vc4 = (199, 144, 0) # note 4


while not keyboard.is_pressed('ctrl'):
    start_time = time.time() # start count time
    px = ImageGrab.grab() # take screenshot

    # Current note color
    color1 = px.getpixel((425, 682)) # note 1
    color2 = px.getpixel((568, 682)) # note 2
    color3 = px.getpixel((712, 682)) # note 3
    color4 = px.getpixel((853, 682)) # note 4

    if color1 == vc1 and v1 == 0:
        keyboard.press(key1)
        v1 = 1
    elif (0, 0, 0) != color1 != vc1 and v1 == 1:
        keyboard.release(key1)
        v1 = 0

    if color2 == vc2 and v2 == 0:
        keyboard.press(key2)
        v2 = 1
    elif (0, 0, 0) != color2 != vc2 and v2 == 1:
        keyboard.release(key2)
        v2 = 0

    if color3 == vc3 and v3 == 0:
        keyboard.press(key3)
        v3 = 1
    elif (0, 0, 0) != color3 != vc3 and v3 == 1:
        keyboard.release(key3)
        v3 = 0

    if color4 == vc4 and v4 == 0:
        keyboard.press(key4)
        v4 = 1
    elif (0, 0, 0) != color4 != vc4 and v4 == 1:
        keyboard.release(key4)
        v4 = 0

    print(f"Finish in: {round(1000 * (time.time() - start_time))} ms ")
winsound.Beep(frequency, duration)
