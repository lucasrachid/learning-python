#EXERCÍCIO 36
#casa = float(input('Qual o valor da casa ? ').strip())
#salario = float(input('Qual o valor da sua renda mensal ? ').strip())
#prazo = int(input('Em quantos anos você quer pagar ? ').strip())
#taxa = casa * 1.30
#minimo = salario * 0.30
#condicao = (taxa/(prazo*12))/salario
#if condicao >= minimo:
#    print('Infelizmente não podemos comprometer mais de 30% de sua renda \ncom financiamento da casa.')
#elif condicao <= minimo:
#    print('Legal, a sua prestação ficará de {:.2f} pelo prazo de {} anos'.format((taxa/(prazo*12)), prazo), end='')
#   print(' ficando o valor total do financiamento em {} reais'.format(taxa))

#EXERCÍCIO 37
#n = int(input('Diga um número inteiro: ').strip())
#escolha = int(input('Escolha 1 para converter em Binário, 2 para Octal e 3 para Hexadecimal: ').strip())
#print('''Escolha a base para conversão, sendo: '
#[1] BINÁRIO
#[2] OCTAL
#[3] HEXADECIMAL''')
#if escolha == 1:
#    print('O número {} convertido para base Binária, fica {}'.format(n, bin(n)[2:]))
#elif escolha == 2:
#    print('O número {} convertido para base Octal, fica {}'.format(n, oct(n)[2:]))
#elif escolha == 3:
#       print('O número {} convertido para base Hexadecimal, fica {}'.format(n, hex(n)[2:]))
#else:
#   print('Preciso que seja apenas um número inteiro entre 1 e 3!')
#print('Até a próxima!')

#EXERCÍCIO 38
#from time import sleep
#n = float(input('Diga um número: ').strip())
#n1 = float(input('Agora diga outro número: ').strip())
#print('Ok, deixa eu analisar...')
#print('Processando...')
#sleep(3)
#if n == n1:
#    print('Os dois valores são iguais!')
#elif n >= n1:
#    print('O Valor {} é maior que {}'.format(n, n1))
#else:
#    print('O valor de {} é menor que {}'.format(n, n1))

#EXERCÍCIO 39
#from datetime import date
#print('Você é Homem ou Mulher ? ')
#print('[1] HOMEM')
#print('[2] MULHER')
#sexo = int(input('Escolha: ').strip())
#if sexo == 1:
#    ano = int(input('Diga em que ano você nasceu ? ').strip())
#    ano1 = date.today().year
#    ano2 = ano1 - ano
#    if ano2 == 18:
#        print('Parabéns, você chegou a maioridade, já está na hora de se alistar!')
#    elif ano2 >= 18:
#        print('Poxa, você já tem {} anos! Você deveria ter se alistado em {}.'.format(ano2, ano + 18))
#    else:
#        print('Calma gafanhoto, quando você completar 18 anos, você poderá se alistar!\n'
#              'Você deverá se alistar em {}'.format(ano + 18))
#else:
#    print('O alistamento feminino não é obrigatório, mas nada impede de você lutar pela nossa nação!')


#EXERCÍCIO 40
#t1 = float(input('Diga a sua média no primeiro trimestre: ').strip())
#t2 = float(input('Diga a sua média no segundo trimestre: ').strip())
#media = (t1 + t2 + t3) / 3
#if media == 70:
#    print('Parabéns, você foi aprovado com a média trimestral de {}.'.format(media))
#elif media <=49:
#    print('Infelizmente você foi reprovado!')
#elif media <= 50 or media <= 69:
#    print('Quem passa direto é trem, você ficou de recuperação!')

#EXERCÍCIO 41
#from datetime import date
#nome = input('Diga qual o nome do atleta: ').strip()
#ano = int(input('Em que ano ele nasceu ? ').strip())
#dia = date.today().year
#cat = dia - ano
#if cat <= 9:
#    print('Ok, o atleta {} irá participar da categoria MIRIM!'.format(nome))
#elif cat <= 14:
#    print('Ok, o atleta {} irá participar da categoria INFANTIL!'.format(nome))
#elif cat <= 19:
#    print('Ok, o atleta {} irá participar da categoria JUNIOR!' .format(nome))
#elif cat <= 20:
#    print('Ok, o atleta {} irá participar da categoria SÊNIOR!'.format(nome))
#else:
#    print('Ok, o atleta {} irá participar da categoria MASTER!'.format(nome))

#EXERCÍCIO 42
#r1 = float(input('Quanto mede a primeira reta ? ').strip())
#r2 = float(input('Quanto mede a segunda reta ? ').strip())
#r3 = float(input('Quanto mede a terceira reta ? ').strip())
#if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
#    print('As retas acima, podem formar um triângulo!')
#    if r1 == r2 == r3:
#        print('EQUILÁTERO')
#    elif r1 != r2 != r3 != r1:
#        print('ESCALENO')
#    else:
#        print('ISÓSCELES')
#else:
#    print('As retas acima, não podem formar um triângulo!')

#EXERCÍCIO 43
#altura = float(input('Quanto de Altura você tem ? ').strip())
#peso = float(input('Quanto você pesa ? ').strip())
#imc = peso / (altura*altura)
#if imc <= 18.5:
#    print('De acordo ao seu IMC de {:.2f}, você está abaixo do peso!'.format(imc))
#elif imc <= 18.5 or imc <= 25:
#    print('De acordo ao seu IMC de {:.2f}, você está no peso ideal!'.format(imc))
#elif imc <= 25 or imc <= 30:
#    print('De acordo ao seu IMC de {:.2f}, você está sobrepeso!'.format(imc))
#elif imc <= 30 or imc <= 40:
#    print('De acordo ao seu IMC de {:.2f}, você está Obeso!'.format(imc))
#else:
#    print('De acordo ao seu IMC de {:.2f}, você está com Obesidade Mórbida!'.format(imc))

#EXERCÍCIO 44
#produto = float(input('Qual o valor do seu produto ? ').strip())
#print('De que maneira você quer pagar, digite (1 - para À Vista - Dinheiro/cheque), (2 - À Vista - Cartão)')
#print('(3 - Parcelado em até 2x no Cartão) ou (4 - Parcelado em 3x ou mais no Cartão)')
#choice = int(input(' ').strip())
#dinheiro = produto - (produto * 0.10)
#cartao1 = produto - (produto * 0.05)
#cartao2 = produto / 2
#cartao3 = produto * 1.2
#if choice == 1:
#    print('Ok, o valor do produto teve 10% de desconto, ficando assim {} reais'.format(dinheiro))
#elif choice == 2:
#    print('Ok, o valor do produto teve 5% de desconto, ficando assim {} reais'.format(cartao1))
#elif choice == 3:
#    print('Ok, infelizmente no cartão em 2x não podemos dar desconto!')
#elif choice == 4:
#    print('Tem certeza que não quer pagar a vista ? O produto teve um acréscimo de 20%, totalizando {} reais.'.format(cartao3))

#EXERCÍCIO 45
from random import randint
from time import sleep
print('Suas opções:\n'
      '[0] PEDRA\n'
      '[1] PAPEL\n'
      '[2] TESOURA')
jogada = int(input('Qual é a sua jogada ? ').strip())
jogadas = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0,2)
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÔ!!')
print('-=-'*10)
if computador == 0:
    if jogada == 0:
        print('O Computador jogou {}\nE o jogador jogou {}, Nós Empatamos!'.format(jogadas[computador], jogadas[jogada]))
    elif jogada == 1:
        print('O Computador jogou {}\nE o jogador jogou {}, Você Venceu!'.format(jogadas[computador], jogadas[jogada]))
    elif jogada == 2:
        print('O Computador jogou {}\nE o jogador jogou {}, Você Perdeu!'.format(jogadas[computador], jogadas[jogada]))
if computador == 1:
    if jogada == 1:
        print('O Computador jogou {}\nE o jogador jogou {}, Nós Empatamos!'.format(jogadas[computador], jogadas[jogada]))
    elif jogada == 0:
        print('O Computador jogou {}\nE o jogador jogou {}, Você Venceu!'.format(jogadas[computador], jogadas[jogada]))
    elif jogada == 2:
        print('O Computador jogou {}\nE o jogador jogou {}, Você Perdeu!'.format(jogadas[computador], jogadas[jogada]))
if computador == 2:
    if jogada == 2:
        print('O Computador jogou {}\nE o jogador jogou {}, Nós Empatamos!'.format(jogadas[computador], jogadas[jogada]))
    elif jogada == 0:
        print('O Computador jogou {}\nE o jogador jogou {}, Você Venceu!'.format(jogadas[computador], jogadas[jogada]))
    elif jogada == 1:
        print('O Computador jogou {}\nE o jogador jogou {}, Você Perdeu!'.format(jogadas[computador], jogadas[jogada]))
elif jogada >=3:
    print('Essa não é uma jogada válida!')
print('-=-'*10)


