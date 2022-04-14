import time

totalscore = 0
print('Quiz Game')
diag = input('Aperte "enter" para começar!')
print('O jogo é simples, 1 pergunta, 5 ou + opções de resposta.')
time.sleep(2)
print('Apenas uma estara correta!')
time.sleep(2)
print('Leia a pergunta e selecione uma das questões como possível resposta.')
time.sleep(2)
print('Para selecionar a pergunta, apenas digite o número da resposta.')
time.sleep(2)
print('Quando você terminar de responder todos os quiz,Será mostrado quantos acertos foram feitos.')
time.sleep(2)
diag = input('O joguinho é apenas isso, após essa mensagem, o jogo começa.')
print('')
time.sleep(1)
print('Quiz 1')
time.sleep(1)
print('')
print('Qual é o jogo que o lucca mais jogou na steam?')
print('1.Counter-Strike:Global Offensive')
print('2.Rocket League')
print('3.Minecraft')
print('4.Scrap Mechanic')
print('5.Roblox')
time.sleep(1)
quiz = input('Digite o número da resposta:')
if quiz == '1':
    print('Correto!')
    totalscore = totalscore + 1
else:
    print('Errado!')
    totalscore = totalscore - 1
    time.sleep(1)
diag = input('Contunue')
print('')
print('Quiz 2')
print('')
time.sleep(1)
print('Quem é a pessoa que tem o pior sentido ou noção no Rocket League?')
print('1.Pangua')
print('2.Lucca')
print('3.Grilo')
print('4.Nando')
print('5.Lone')
print('6.Brugam')
quiz = input('Digite o número da resposta:')
if quiz == '5':
    print('Correto!')
    totalscore = totalscore + 1
else:
    print('Errado!')
    totalscore = totalscore - 1
    time.sleep(1)
diag = input('Continue')
print('')
print('Quiz 3')
print('')
time.sleep(1)
print('Viciado em Crypto Moedas.')
print('1.Brugam')
print('2.Hyurhii')
print('3.Ali (AoiDrake2)')
print('4.AKings')
print('5.Pangua')
quiz = input('Digite o número da resposta:')
if quiz == '5':
    print('Correto! Pangua é')
    totalscore = totalscore + 1
else:
    print('Errado!')
    totalscore = totalscore - 1
print('')
time.sleep(1)
diag = input('Continue')
print('')
print('Quiz 4')
print('')
time.sleep(1)
diag = input('conhecimento sobre jogo.')
print('É possivel zerar o Minecraft em um mundo de modo Adventure?')
print('1.sim')
print('2.Não')
print('3.Sim?')
print('4.Não sei.')
print('5.Óbvio que não, que pergunta idiota.')
quiz = input('Digite o número da resposta:')
if quiz == '1':
    print('Correto! É possivel zerar.')
    totalscore = totalscore + 1
elif quiz == '3':
    print('Não é você que pergunta!...(-2 pontos)')
    totalscore = totalscore - 2
elif quiz == '4':
    print('Não sabe?')
    totalscore = totalscore + 0
elif quiz == '5':
    print('Qual foi a sua conclusão para chegar nessa resposta!?')
    totalscore = totalscore - 10
else:
    print('Errado!')
    totalscore = totalscore - 1
print('')
time.sleep(1)
diag = input('Continue')
print('')
print('Quiz 5')
print('')
time.sleep(1)
print('Item mais difícil de pegar no minecraft.')
print('1.Obsidian')
print('2.Diamante')
print('3.Beacon')
print('4.Bloco de netherite')
print('5.cabeça de esqueleto de wither')
print('6.elytra')
quiz = input('Digite o número da resposta:')
if quiz == '4':
    print('Correto!')
    totalscore = totalscore + 2
else:
    print('Errado!')
    totalscore = totalscore - 1
print('')
time.sleep(1)
diag = input('Continue')
print('')
print('Quiz 6')
print('')
time.sleep(1)
print('Qual é o servidor de discord é o mais antigo?')
print('1.Senhor da Madrugada')
print('2.?')
print('3.Servidor BTS')
print('4.Gataria')
print('5.Império da Madrugada')
print('6.Universe da Zueira')
print('7.Servidor TBS')
quiz = input('Digite o número da resposta:')
if quiz == '5':
    print('Correto!')
    totalscore = totalscore + 1
elif quiz == '1':
    print('com certeza, esta certissímo!')
    totalscore = totalscore - 5
elif quiz == '3':
    print('Não sabia que existia um servidor BTS')
    totalscore = totalscore - 8
elif quiz == 2:
    print('@!$!$??!?@$??2#$@#$@$')
    totalscore = totalscore + 19383939389281234
else:
    print('Errado!')
    totalscore = totalscore - 1


print('')
print('Jogo acabou. (Por enquanto)')
print('Total de Pontos:', totalscore)
