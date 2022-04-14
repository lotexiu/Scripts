import time
import keyboard
import mido
import os

# 62 = 38 (D)
# != = -24
#os.system('start chrome.exe https://virtualpiano.net/')

keys = ['1', 'shift + 1', '2', 'shift + 2', '3', '4', 'shift + 4', '5', 'shift + 5', '6', 'shift + 6',
        '7', '8', 'shift + 8', '9', 'shift + 9', '0', 'q', 'shift + q', 'w', 'shift + w', 'e', 'shift + e',
        'r', 't', 'shift + t', 'y', 'shift + y', 'u', 'i', 'shift + i', 'o', 'shift + o', 'p', 'shift + p',
        'a', 's', 'shift + s', 'd', 'shift + d', 'f', 'g', 'shift + g', 'h', 'shift + h', 'j', 'shift + j',
        'k', 'l', 'shift + l', 'z', 'shift + z', 'x', 'c', 'shift + c', 'v', 'shift + v', 'b', 'shift + b',
        'n', 'm']

while True:
    while True:
        songs = []
        list = os.listdir('.')
        for mids in list:
            if '.mid' in mids:
                songs += [mids]

        low = 200
        higher = -100
        print('Songs:')
        for show in range(len(songs)):
                print(f'({show}) {songs[show]}')
        print('\nType "!exit" to close')
        print("Some songs may not work properly")
        choice = input('Chosse your song: ')
        if choice == '!exit':
            exit()
        else:
            choice = int(choice)
        mid = mido.MidiFile(f'{songs[choice]}')
        count_on = 0
        count_off = 0
        for msg in mid:
            msg = str(msg)
            if 'note_on' in msg:
                count_on += 1
            if 'note_off' in msg:
                count_off += 1
        if count_on != count_off:
            print('This song is currupted\n')
            os.system(f'del "{songs[choice]}"')
            time.sleep(1)
        else:
            for msg in mid:
                msg = str(msg)
                if 'note_on' in msg:
                    valor = msg[23:26]
                    y = ''
                    for fix in valor:
                        if fix in str((1, 2, 3, 4, 5, 6, 7, 8, 9, 0)):
                            y += fix
                    x = int(y) - 24
                    if x < low:
                        low = x
                    if x > higher:
                        higher = x

            max = len(keys) - 1
            note = 24 + low
            higher -= low
            if higher > max:
                print("\nis bigger than the piano!")
                print('you can try playing it but it might not work right.')
                time.sleep(1)
            break
    print(f'\nselected: {songs[choice]}\n')
    print('Song is ready! press "scrlk" to start!')
    print('Press Delete to Stop!')
    while True:
        if keyboard.is_pressed('scrlk'):
            keyboard.release('scrlk')
            break
        time.sleep(0.1)

    for msg in mid.play():
        msg = str(msg)
        if 'note_on' in msg:
            x = int(msg[23:26]) - note
            if x > max:
                x -= (higher - max)
            keyboard.press(keys[x])
        if 'note_off' in msg:
            x = int(msg[24:27]) - note
            if x > max:
                x -= (higher - max)
            keyboard.release(keys[x])
        if keyboard.is_pressed('del'):
            keyboard.release('del')
            for soltar in keys:
                keyboard.release(soltar)
            break
