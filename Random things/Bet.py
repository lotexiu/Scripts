import os
import time

vezes = 0
start = 0
if os.path.isfile('system.py'):
    import system
    system1 = open('system.py', 'r')
    start = system.start


nota = open("C:/Users/aleph/Desktop/nota.txt", "a")

for linejump in range(start):
    nota.write("\r")

nota.write('tecla = [')
print('Para sair, digite "Sair".')
for line in range(1000):

    tecla_d = input("item %s:" % vezes)
    if not (tecla_d == 'Sair') and (vezes >= 1):
        nota.write(', ')
    if tecla_d == 'Sair':
        break
    nota.write("'")
    nota.write(tecla_d)
    nota.write("'")
    vezes += 1

nota.write(']')
nota.close()
start += 1
system1 = open('system.py', 'w')
system1.write('start = %s' % start)
system1.close()

os.system("C:/Users/aleph/Desktop/nota.txt")
for closing in range(10):
    print('Fechando arquivo em:', 10 - closing)
    time.sleep(1)
os.system('taskkill/im notepad.exe')