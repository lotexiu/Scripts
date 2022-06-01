import time
import keyboard
import mido
import os

all_keys = ['esc', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'PrtScn',
            'ScrLk', 'Num -', '"', '-', '+', 'Backspace', 'insert', 'home', 'PageUp', 'Enter', '/', 'del',
            'left arrow', 'up arrow', 'down arrow', 'right arrow', 'insert', 'end', 'PageDown', 'Ctrl',
            'Shift', 'CapsLock', 'tab', '|', '<', '>', ':', '´', '[', '~', ']', 'Alt']


keys = ['1', 'shift + 1', '2', 'shift + 2', '3', '4', 'shift + 4', '5', 'shift + 5', '6', 'shift + 6',
        '7', '8', 'shift + 8', '9', 'shift + 9', '0', 'q', 'shift + q', 'w', 'shift + w', 'e', 'shift + e',
        'r', 't', 'shift + t', 'y', 'shift + y', 'u', 'i', 'shift + i', 'o', 'shift + o', 'p', 'shift + p',
        'a', 's', 'shift + s', 'd', 'shift + d', 'f', 'g', 'shift + g', 'h', 'shift + h', 'j', 'shift + j',
        'k', 'l', 'shift + l', 'z', 'shift + z', 'x', 'c', 'shift + c', 'v', 'shift + v', 'b', 'shift + b',
        'n', 'm']


def transpose():
    print('\nHotkeys like "Shift + t" or "Num 1", do not work.')
    print('Need to be just one key. Few keys that can be used.')
    print('Hit the hotkey that decreases Transpose!')

    stop = 0
    while True:
        for key in all_keys:
            if keyboard.is_pressed(key):
                print(f'\nYour Key is: {key}')
                down_transpose = key
                diag = input('Thats correct? Y or N?')
                if diag.lower() == 'y':
                    stop = 1
                    break
                else:
                    print('Try Again.')
        if stop == 1:
            break
        time.sleep(0.3)

    time.sleep(1)
    print('Hit the hotkey that increases Transpose!')
    stop = 0
    while True:
        for key in all_keys:
            if keyboard.is_pressed(key):
                print(f'\nYour Key is: {key}')
                up_transpose = key
                diag = input('Thats correct? Y or N?')
                if diag.lower() == 'y':
                    stop = 1
                    break
                else:
                    print('Try Again.')
        if stop == 1:
            break
        time.sleep(0.3)
    return down_transpose, up_transpose


def paginas(Midi_list):
    pags = 0
    while True:
        pags += 1
        if pags * 12 >= len(Midi_list):
            break
    return pags


def mostrar(pag, Midi_list):
    print()
    for musicas in range(12):
        val = musicas + (12 * (int(pag[-1]) - 1))
        print(f'({val + 1}) {Midi_list[val]}')
        if Midi_list[val] == Midi_list[-1]:
            break


while True:
    songs = []
    listar = os.listdir('.')
    for mids in listar:
        if '.mid' in mids:
            songs += [mids]

    choose = '1'
    low = 200
    higher = -100
    maxpags = paginas(songs)
    mostrar('1', songs)
    while True:
        print(f'\n{"-"*10}| Page {choose[-1]}/{maxpags} |{"-"*10}')
        print('Type p"number" to change page. Ex: p2')
        print('type the number to select the song.')
        print('Type "!exit" to close.')
        choose = input('Choose:')
        choose = choose.lower()
        if 'p' in choose:
            if int(choose[1]) > maxpags:
                print('Does not exist this page.')
            else:
                mostrar(choose, songs)
        elif choose == '!exit':
            exit()
        elif choose.isalpha() or int(choose) > len(songs):
            print('What?..')

        elif 'p' not in choose:
            mid = mido.MidiFile(f'{songs[int(choose) - 1]}')
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
            normal = []
            num_up = []
            num_down = []
            if higher > max:

                print("\nIs bigger than the piano!")
                print('May not work on non-transpose pianos.')
                while True:
                    question = input("Does your virtual piano have Transpose? Y or N? ")
                    if question.lower() == 'y':
                        down_transpose, up_transpose = transpose()
                        break

                    elif question.lower() == 'n':
                        for loop in range(higher + 1):
                            if loop // 1.12 not in normal:
                                normal += [loop // 1.12]
                            else:
                                if (loop // 1.12) - 1 not in normal:
                                    if int(loop) != 1:
                                        num_down += [int(loop)]
                                if (loop // 1.12) + 1 not in normal:
                                    num_up += [int(loop)]
                        break
                    else:
                        print('What?..')
        if 'p' not in choose:
            break

    print(f'\nselected: {songs[int(choose) - 1]}\n')
    print('Song is ready! press "scrlk" to start!')
    print('Press Delete to Stop!')
    while True:
        if keyboard.is_pressed('scrlk'):
            keyboard.release('scrlk')
            break
        time.sleep(0.3)
    print('Running...')

    count_on = 0
    count_off = 0

    for msg in mid:
        msg = str(msg)
        if 'note_on' in msg:
            count_on += 1
        elif 'note_off' in msg:
            count_off += 1

    if count_on != count_off:  # if have only ON
        for x in range(120):
            exec(f'note{x} = 0')

        for msg in mid.play():
            msg = str(msg)
            if 'note_on' in msg:
                valor = msg[23:26]
                y = ''
                for fix in valor:
                    if fix in str((1, 2, 3, 4, 5, 6, 7, 8, 9, 0)):
                        y += fix

                if higher > max:
                    if int(y) in num_up:
                        x = int((int(y) - note) // (1 + 0.015 * (higher - max)) + 1)
                    if int(y) in num_down:
                        x = int((int(y) - note) // (1 + 0.015 * (higher - max)) + 1)
                    else:
                        x = int((int(y) - note) // (1 + 0.015 * (higher - max)))

                else:
                    x = int(y) - note
                if eval(f'note{x}') == 0:  # press
                    if x > max:
                        x = max
                    keyboard.press(keys[x])
                    exec(f'note{x} = 1')

                elif eval(f'note{x}') == 1:  # release
                    keyboard.release(keys[x])
                    exec(f'note{x} = 0')

                if keyboard.is_pressed('del'):  # stop
                    keyboard.release('del')
                    print('Stopped')
                    for soltar in keys:
                        keyboard.release(soltar)
                    break

    else:  # if have ON and OFF
        for msg in mid.play():
            msg = str(msg)
            if 'note_on' in msg:
                valor = msg[23:26]
                y = ''
                for fix in valor:
                    if fix in str((1, 2, 3, 4, 5, 6, 7, 8, 9, 0)):
                        y += fix

                if higher > max:
                    if int(y) in num_up:
                        x = int((int(y) - note) // (1 + 0.015 * (higher - max)) + 1)
                    if int(y) in num_down:
                        x = int((int(y) - note) // (1 + 0.015 * (higher - max)) + 1)
                    else:
                        x = int((int(y) - note) // (1 + 0.015 * (higher - max)))
                else:
                    x = int(y) - note

                if x > max:
                    x = max
                keyboard.press(keys[x])
            if 'note_off' in msg:
                y = ''
                for fix in valor:
                    if fix in str((1, 2, 3, 4, 5, 6, 7, 8, 9, 0)):
                        y += fix

                valor = msg[23:26]
                if higher > max:
                    if int(y) in num_up:
                        x = int((int(y) - note) // (1 + 0.015 * (higher - max)) + 1)
                    if int(y) in num_down:
                        x = int((int(y) - note) // (1 + 0.015 * (higher - max)) + 1)
                    else:
                        x = int((int(y) - note) // (1 + 0.015 * (higher - max)))
                else:
                    x = int(y) - note

                keyboard.release(keys[x])
            if keyboard.is_pressed('del'):
                keyboard.release('del')
                print('Stopped')
                for soltar in keys:
                    keyboard.release(soltar)
                break