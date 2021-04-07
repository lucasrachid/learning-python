#EXERCÍCIO 28
#s = input('Escreva "start" para iniciar: ').strip().upper()
#if s == 'START':
#    print('INICIANDO...')
#    import random
#    lista = [1, 2, 3, 4, 5]
#    num = random.choice(lista)
#    print('EMBARALHANDO NÚMEROS...')
#    chute = int(input('Escolha um número entre 1 a 5, se for igual ao que \n o computador escolher, você ganha: ').strip())
#    print('O número escolhido pelo computador é {}'.format(num))
#    if num == chute:
#        print('PARABÉNSSS, VOCÊ É FODA')
#    else:
#        print('Você perdeu, boa sorte na próxima')
#else:
#    print('Ok, até a próxima!!')

#EXERCÍCIO 28 CORRIGIDO
from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar!')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei ? ').strip()) #Jogador tenta adivinhar.
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}'.format(computador, jogador))