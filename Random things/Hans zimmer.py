import os
import webbrowser
import time
import keyboard

#webbrowser.open('https://virtualpiano.net/')

combo = ['6+0+e+u', '7+r+u', '6+0+e+u', '7+r+u', '8+w+t+u', '7+r+u',
         '6+0+e+u', '7+r+u', '8+w+t+u', '7+r+u', '4+8+q+e+u+p', 'u+f', 'e+u+p', 'u+f',
         '5+9+w+r+u+a', 'u+f', 'r+u+a', 'u+f', '6+0+e+t+u+s', 'u+f', 't+u+s', 'u+f',
        '5+9+w+y+o+d', 'u+f', 'y+o+d', 'u+a+f', 'r+u+a', '4+8+q+e+u+p', 'u+f', 'e+p', 'e+p',
        'u+f', 'e+u+p', '5+9+w+r+u+a', 'u+f', 'r+a', 'r+a', 'u+f', 'r+u+a', '6+0+e+t+u+s',
         'u+f', 't+s', 't+s', 'u+f', 't+u+s', '5+9+w+y+o+d', 'u+f', 'y+d', 'y+o+d', 'u+a+f',
         'r+u+a', '0+u+f+x', '4+8+q+s+l', '5+9+w+d+z', '4+8+q+s+l', '5+9+w+d+z', '6+0+e+u+f', '6+u', '0+u',
         '6+u', '0+u', '7+u', '0+u', '7+u', '0+u', '8+u', '0+u', '8+u', '0+u', '9+u', '0+u',
         '4+8+q+p', '5+9+w+a', '6+0+e+s', '5+9+w+d', 'q+p+j', 'u+f+x', 'q+p+j', 'u+f+x', 'w+a+k', 'u+f+x',
         'w+a+k', 'u+f+x', 'e+s+l', 'u+f+x', 'e+s+l', 'u+f+x', 'w+d+z', 'u+f+x''w+d+z', 'u+f+x''u+a+k',
         'q+p+j', 'u+f+x', 'u+p+j', 'q+p+j', 'u+f+x', 'u+p+j', 'w+a+k', 'u+f+x''u+a+k', 'w+a+k', 'u+f+x',
         'u+a+k', 'e+s+l', 'u+f+x', 'u+s+l', 'e+s+l', 'u+f+x', 'u+s+l', 'w+d+z', 'u+f+x''u+d+z', 'w+d+z',
         'u+f+x''u+a+k', '4+8+q+p+s+f+j', '5+9+w+a+s+f+k', '6+0+e+s+f+l', '5+9+w+s+d+hz', '3+0+f+x', 'u+p+j', 'u+a+k',
         'e+u+p+j', 'r+u+a+k', 't+u+s+l', 'r+u+a+k', 'e+u+p+j', 'r+u+a+k', 't+u+s+l', 'y+u+d+z', '3+0+f+x']


rep = 0
repetição = [15, 3, 8]
nota1 = ['u', 't', 'y', 't']
nota2 = ['t', 'u', 'u', 'y']

#keyboard.press_and_release('shift+s, space')
time.sleep(3)
for song1 in range(3):
    for song in range(repetição[rep]):
        keyboard.press_and_release(nota1[rep])
        time.sleep(0.35)
        keyboard.press_and_release(nota2[rep])
        time.sleep(0.35)
        if keyboard.is_pressed('esc'):
            break
    keyboard.press_and_release(combo[rep])
    rep += 1
    ret = rep + 1
for song2 in range(2):
    keyboard.press_and_release(nota1[rep])
    time.sleep(0.35)
    keyboard.press_and_release(combo[rep])
    time.sleep(0.35)
    keyboard.press_and_release(nota2[rep])
    time.sleep(0.35)
    print('part 1')
    if ret == 4:
        keyboard.press_and_release(combo[ret])
        time.sleep(0.35)
        keyboard.press_and_release(nota2[rep])
        time.sleep(0.35)
        ret += 1
        keyboard.press_and_release(combo[ret])
        time.sleep(0.35)
        keyboard.press_and_release(nota2[rep])
        time.sleep(0.35)
        ret += 1
        keyboard.press_and_release(combo[ret])
        time.sleep(0.35)
        print('part 2')
    




    
'''   
    if keyboard.is_pressed('esc'):
        break
'''