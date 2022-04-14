import time
import keyboard
from PIL import Image, ImageGrab
import winsound
frequency = 100  # Set Frequency To 2500 Hertz
duration = 80  # Set Duration To 1000 ms == 1 second


v1 = 0
v2 = 0
v3 = 0
v4 = 0
vc1 = (255, 255, 0)
vc2 = (255, 0, 0)
vc3 = (0, 255, 255)
vc4 = (0, 255, 120)


while not keyboard.is_pressed('ctrl'):
    start_time = time.time()

    px = ImageGrab.grab().load()
    color1 = px[439, 664] # centro da nota
    color2 = px[575, 664] # centro da nota
    color3 = px[706, 664] # centro da nota
    color4 = px[842, 664] # centro da nota

    line_color1 = px[438, 664] # inicio da linha
    line_color2 = px[574, 664] # inicio da linha
    line_color3 = px[705, 664] # inicio da linha
    line_color4 = px[841, 664] # inicio da linha

    if color1 == vc1 and v1 == 0:
        keyboard.press('a')
        v1 = 1
    if color2 == vc2 and v2 == 0:
        keyboard.press('s')
        v2 = 1
    if color3 == vc3 and v3 == 0:
        keyboard.press('j')
        v3 = 1
    if color4 == vc4 and v4 == 0:
        keyboard.press('k')
        v4 = 1

    if line_color1 != vc1 and v1 == 1:
        keyboard.release('a')
        v1 = 0
    if line_color2 != vc2 and v2 == 1:
        keyboard.release('s')
        v2 = 0
    if line_color3 != vc3 and v3 == 1:
        keyboard.release('j')
        v3 = 0
    if line_color4 != vc4 and v4 == 1:
        keyboard.release('k')
        v4 = 0

    print(f"Finish in: {round(1000 * (time.time() - start_time))} ms ")
winsound.Beep(frequency, duration)