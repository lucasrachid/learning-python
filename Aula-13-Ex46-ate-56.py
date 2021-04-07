#EXERCÍCIO 46
#import emoji
#from time import sleep
#print('Chegou o Ano novo, a contagem dos fogos irá iniciar')
#print('Escreva "START" para iniciar a contagem!')
#iniciar = input(' ').strip().upper()
#if iniciar == 'START':
#    for c in range (10, 0, -1):
#        print(c)
#        sleep(1)
#else:
#    for c in range (10, 0, -1):
#        print(c)
#        sleep(1)
#print('BOMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
#print(emoji.emojize(':\U0001f386:'))

#EXERCÍCIO 47
#for c in range (2, 50+1, 2):
#    print(c)

#EXERCÍCIO 48
#soma = 0 #Acumulador
#quantidade = 0 #Contador
#for c in range (1, 500, 2):
#    if c % 3 == 0:
#        soma += c
#        quantidade = quantidade + 1
#print('A soma dos {} números múltiplos de 3 foi {}'.format(quantidade, soma))

#EXERCÍCIO 49
#n = int(input('Escolha um número: '))
#for c in range (1, 11):
#    print('{} x {} = {}'.format(n, c, n*c))

#EXERCÍCIO 50
#soma = 0
#for c in range (0, 6):
#    n = int(input('Digite um valor: '))
#    if n % 2 == 0:
#        soma += n
#print('A soma dos números pares foi {}'.format(soma))

#EXERCÍCIO 51
#pt = int(input('Diga o primeiro termo: '))
#r = int(input('Diga o valor da razão: '))
#for c in range (pt, 10*r, r):
#    print(c, end=' => ')
#print('Acabou!')

#EXERCÍCIO 52
#total = 0
#n = int(input('Digite um número para verificar se é primo: '))
#for c in range(1, n + 1):
#    if n % c == 0:
#        print('\033[33m', end=' ')
#        total += 1
#    else:
#        print('\033[32m', end=' ')
#    print('{} '.format(c), end='')
#if total == 2:
#    print('\n\033[mO número {} pode ser dividido até em {} vezes, portanto é um número primo!'.format(n, total))
#else:
#    print('O número {} pode ser dividido até em {} vezes, portanto não é um número primo!'.format(n, total))

#EXERCÍCIO 53
#frase = str(input('Digite uma frase e veja se ela é um palíndromo: ').replace(' ', '')).upper().strip()
#inverso = ''
#for c in range(len(frase) -1, -1, -1):
#    inverso += frase[c]
#print('A frase junta é: {} e invertida é: {}.'.format(frase, inverso))
#if frase == inverso:
#    print('A frase é um palíndromo!')
#else:
#    print('A frase não é um palíndromo!')

#EXERCÍCIO 54
#from datetime import date
#cont = 0
#cont1 = 0
#ano = date.today().year
#for c in range(1, 8):
#    ano2 = int(input('Em que ano nasceu a {}º pessoa?  '.format(c)))
#    maior = ano - ano2
#    if maior >= 18:
#        cont += 1
#    else:
#        cont1 += 1
#print('Ao todo tivemos {} pessoas maiores de idade'.format(cont))
#print('E também tivemos {} pessoas menores de idade'.format(cont1))

#EXERCÍCIO 55
#maior = 0
#menor = 0
#for c in range (1, 6):
#    peso = float(input('Qual o peso da {}º pessoa ? '.format(c)))
#    if c == 1:
#        maior = peso
#        menor = peso
#    else:
#        if peso > maior:
#            maior = peso
#        if peso < menor:
#            menor = peso
#print('O maior peso é {} e o menor peso é {}'.format(maior, menor))

#EXERCÍCIO 56
somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = ''
totmulher20 = 0
for c in range (1, 5):
    print('----- {}º PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: ').strip())
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm' :
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridade, nomevelho))
print('Ao todo, são {} mulheres com menos de 20 anos.'.format(totmulher20))



























