from pyautogui import *
import pyautogui
import time
import keyboard

from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)


print('p = show position mouse and color')
print('You just need click one time')


while True:
    if keyboard.is_pressed('p'):
        x, y = pyautogui.position()
        im = pyautogui.screenshot()
        r, g, b = im.getpixel((x, y))
        print(f' x,y = {x, y} RGB = {r, g, b}')
        time.sleep(0.5)
    time.sleep(0.1)


'''
while True:
    start_time = time.time()
    while True:
        if round(1000 * (time.time() - start_time)) > 3:
            break
    print(f"Finish in: {round(1000 * (time.time() - start_time))} ms ")
    
'''