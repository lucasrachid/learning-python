#EXERCÍCIO 28
s = input('Escreva "start" para iniciar: ').strip().upper()
if s == 'START':
    print('INICIANDO...')
    import random
    lista = [1, 2, 3, 4, 5]
    num = random.choice(lista)
    print('EMBARALHANDO NÚMEROS...')
    chute = int(input('Escolha um número entre 1 a 5, se for igual ao que \n o computador escolher, você ganha: ').strip())
    print('O número escolhido pelo computador é {}'.format(num))
    if num == chute:
        print('PARABÉNSSS, VOCÊ É FODA')
    else:
        print('Você perdeu, boa sorte na próxima')
else:
    print('Ok, até a próxima!!')