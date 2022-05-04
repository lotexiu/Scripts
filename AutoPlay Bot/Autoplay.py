import time
import keyboard
from PIL import Image, ImageGrab
import winsound

print('WARNING: Your game needs to be on the main screen (primary screen) to work.')
print('And you need to quote the color of your note in R.G.B. ex: 199,144,0')
print('Link for you see: https://prnt.sc/o5lhLo6w7LDO\n')

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

def pos_notes(num):
    import pyautogui
    import time
    import keyboard

    print(f'Put your mouse in the center of the note {num} and press P')
    print('Click one time')

    while True:
        if keyboard.is_pressed('p'):
            x, y = pyautogui.position()
            print(f' x,y = {x, y}')
            break
        time.sleep(0.1)
    time.sleep(0.8)
    print('Defined!\n')
    return x, y

pos_note1 = pos_notes(1)
pos_note2 = pos_notes(2)
pos_note3 = pos_notes(3)
pos_note4 = pos_notes(4)

while not keyboard.is_pressed('ctrl'):
    start_time = time.time() # start count time
    px = ImageGrab.grab() # take screenshot

    # Current note color
    color1 = px.getpixel((pos_note1)) # note 1
    color2 = px.getpixel((pos_note2)) # note 2
    color3 = px.getpixel((pos_note3)) # note 3
    color4 = px.getpixel((pos_note4)) # note 4

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
