#variavel.pop() remove a ultimo elemento
#variavel.pop(0) remove o primeiro elemento

'''
myList = [2, 1, 3, 5, 1, 1, 1, 0, 4]
print(myList)
myList.clear
print(myList)
'''
'''
remove = int(input('Escolha 1 á 5 para remover:'))

try:
    while True:
        myList.remove(remove)
except ValueError:
    pass
print(myList)

print(100 * '-')

print('part 1 (alterando o valor)')
# alterando o valor no resultado
# lista_nums = [1,2,3,4]
lista_nums = range(4)
for item in lista_nums:
    print(item + 1000)
print('lista num =', lista_nums)

print(100 * '-')

# alterando o valor na lista
lista_nums = [1, 2, 3, 4]
print('lista num (Inicial) =', lista_nums)
for item in range(len(lista_nums)):
    lista_nums[item] += 1000
    print(lista_nums[item])
print('lista num (Final) =', lista_nums)

print(100 * '-')

# alterando o valor na lista
lista_nums = [1, 2, 3, 4]
print('lista num (Inicial) =', lista_nums)
for idx, item in enumerate(lista_nums):
    lista_nums[idx] += 1000
    print(lista_nums[idx])
print('lista num (Final) =', lista_nums)
print('removendo o ultimo')
del lista_nums[-1]
print(lista_nums)
print(100 * '-')

# alterando o valor na lista e colocando quantidade aleatoria dentro da lista
quantia = int(input('1 até? ')) + 1
lista_nums = list(range(1, quantia))
print('lista num (Inicial) =', lista_nums)
for item in range(len(lista_nums)):
    lista_nums[item] += 1000
    print(lista_nums[item])
print('lista num (Final) =', lista_nums)

print(100 * '-')

print('part 2 [Começa:Termina:Remove Ou pula]')
lista_joken = 'Rock, Paper or Scissor'
print('Lista:', lista_joken)
print('invertido:', lista_joken[::-1])
print('removendo a segundo caractere:', lista_joken[::2])
print('terminando na 10º caractere:', lista_joken[:20])
print('Começando no 5º caractere:', lista_joken[5:30])
print('Lista:', lista_joken)
lista_joken = lista_joken[5:30]
print('Lista:', lista_joken)

print(100 * '-')

import webbrowser
import os
from pynput import keyboard

# webbrowser.open('https://youtu.be/usE7pgMEj6k?t=0')musica

nota = open("C:/Users/aleph/Desktop/nota.txt", "w")
numbers = 10
for line in range(numbers + 1):
    nota.write("%s\r" % line)
nota.close()
os.system("C:/Users/aleph/Desktop/nota.txt")


'''