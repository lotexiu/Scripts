import shocurasy
import keyboard
import os

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
            sheet, tempo = shocurasy.read_midi(f'{songs[int(choose) - 1]}')
            print(f'\nselected: {songs[int(choose) - 1]}\n')
            print('Song is ready! press "scrlk" to start!')
            print('Press "Pause" to Pause/Resume')
            print('Press Delete to Stop!')
            tom = 0 # Default 0
            while True:
                if keyboard.is_pressed('scrlk'):
                    break
                shocurasy.tempo(200)
            shocurasy.play_sheet(sheet, tempo, tom)
            break