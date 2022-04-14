import time
import keyboard
import os
import winsound
frequency = 220  # Set Frequency To 2500 Hertz
duration = 80  # Set Duration To 1000 ms == 1 second


print(' Press Shift to start AutoPlay')
print(f' Press Ctrl to close AutoPlay')
print(' Press Scrlk to close Menu AutoPlay')
print(' safe mode = Ctrl + F ( you can use ctrl and shift normaly )')

while not keyboard.is_pressed('Scrlk'):
    if keyboard.is_pressed('shift'):
        os.system('start /min python Autoplay.py')
        print('Auto Play ativo')
        winsound.Beep(frequency, duration)
        time.sleep(0.4)
    if keyboard.is_pressed('Ctrl + f'):
        print(' you are in the safe mode')
        winsound.Beep(500, 50)
        time.sleep(0.4)
        while True:
            if keyboard.is_pressed('Ctrl + f'):
                print(' you are leaving safe mode')
                winsound.Beep(400, 50)
                winsound.Beep(600, 50)
                time.sleep(0.4)
                break
            time.sleep(0.3)
    time.sleep(0.3)

winsound.Beep(400, 50)
winsound.Beep(300, 50)
winsound.Beep(200, 50)
winsound.Beep(100, 50)