import Shotokatan as shocurasy
import keyboard

while True:
    songs = shocurasy.search_files('.mid', '../MidiPlayer')
    total_pags = shocurasy.pags(songs, 12)
    choose = '!p1'
    shocurasy.show_pages(songs, total_pags, choose, )
    while True:
        print('Type !p"number" to change page. Ex: !p2')
        print('type the number to select the song.')
        print('Type "!exit" to close.')
        choose = input('Choose:')

        if '!p' in choose.lower():
            songs = shocurasy.search_files('.mid', '../MidiPlayer')
            total_pags = shocurasy.pags(songs, 12)
            shocurasy.show_pages(songs, total_pags, choose, )
        elif choose == '!exit':
            exit()
        elif choose.isnumeric():
            sheet, tempo = shocurasy.read_midi(f'{songs[int(choose) - 1]}')
            print(f'\nselected: {songs[int(choose) - 1]}\n')
            print('Song is ready! press "scrlk" to start!')
            print('Press "Pause" to Pause/Resume')
            print('Press Delete to Stop!')
            tom = -12 # Default -12
            while True:
                if keyboard.is_pressed('scrlk'):
                    break
                shocurasy.tempo(200)
            shocurasy.play_sheet(sheet, tempo, tom)
            break
        else:
            songs = shocurasy.search_files('.mid', '../MidiPlayer')
            total_pags = shocurasy.pags(songs, 12)
            shocurasy.show_pages(songs, total_pags, '!p1', choose)