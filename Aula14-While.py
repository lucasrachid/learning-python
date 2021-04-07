#c=1
#while c!=10:
#    print(c)
#    c+=1
#print('Acabou')

#n = 1
#r = 'S'
#while r == 'S':
#    n = int(input('Digite um número: '))
#    r = str(input('Quer continuar ? [S/N] ')).upper()
#print('Fim')

'''n = 1
par = impar = 0
acumulador = 0
while n != 0:
    n = int(input('Digite um número: ').strip())
    if n != 0:
        if n % 2 == 0:
            par += 1
            acumulador += n
        else:
            impar += 1
            acumulador += n
print('Você digitou {} números pares e {} números ímpares, totalizando {}'.format(par, impar, acumulador))'''

#EXERCÍCIO 57
'''sexo = str(input('Informe o seu sexo: [F/M] ')).upper().strip()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Por favor, informe o seu sexo: ')).strip().upper()
print('Sexo {} registrado com sucesso.'.format(sexo))'''

#EXERCÍCIO 58
'''from random import randint
from time import sleep
computador = randint(0, 10) #Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10, tente adivinhar!')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei ? ').strip()) #Jogador tenta adivinhar.
print('PROCESSANDO...')
sleep(1)
contador = 1
while jogador != computador:
    jogador = int(input('Desculpe, você errou, tente novamente: '))
    contador += 1
    print('PROCESSANDO...')
    sleep(1)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
    print('Mas foram necessárias {} tentativas.'.format(contador))'''

#EXERCÍCIO 59
from time import sleep
choice = 0
while choice!= 5:
    print('Olá, sou sua assistente virtual e vamos re-analisar os números!')
    sleep(1)
    n1 = int(input('Diga um número inteiro: ').strip())
    sleep(1)
    n2 = int(input('Diga outro número inteiro: '))
    sleep(1)
    choice = int(input('MENU:\n[1]SOMAR \n[2]MULTIPLICAR \n[3]MAIOR \n[4]NOVOS NÚMEROS \n[5]SAIR DO PROGRAMA\nOPÇÃO: '))
    sleep(1)
    while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
        choice = int(input('Desculpe, {} não é uma opção valida! escolha novamente: '.format(choice)))
        sleep(1)
    if choice == 1:
        print('A soma do número {} e o número {} é o número {}'.format(n1, n2, (n1 + n2)))
        sleep(1)
    if choice == 2:
        print('A multiplicação do número {} e o número {}, resulta no número {}'.format(n1, n2, (n1 * n2)))
        sleep(1)
    if choice == 3:
        if n1 > n2:
            print('O número {} é o maior!'.format(n1))
            sleep(1)
            print('Reiniciando aplicação...')
            sleep(1)
        elif n1 == n2:
            print('O número {} e o número {} são iguais!'.format(n1, n2))
            sleep(1)
            print('Reiniciando aplicação...')
            sleep(1)
        else:
            print('O número {} é o maior!'.format(n2))
            sleep(1)
            print('Reiniciando aplicação...')
            sleep(1)
    if choice == 4:
        print('Aguarde um momento...')
        sleep(1)
    if choice ==5:
        print('Ok, até a próxima')






