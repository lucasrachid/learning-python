#EXERCÍCIO 30
n = int(input('Digite um número inteiro: ').strip())
resto = n % 2
if resto == 0:
    print('Número é par!')
else:
    print('Número ímpar!')

#EXERCÍCIO 31
#print('Bem vindo ao gerador de passagens!')
#km = float(input('Quantos KM tem a sua viagem ? ').strip())
#if km <= 200:
#    cob = km*0.5
#    print('O preço da sua viagem será de {} reais'.format(cob))
#else:
#    cob1 = km*0.45
#    print('O preço da sua viagem será de {} reais'.format(cob1))

#EXERCÍCIO 32
#from datetime import date
#ano = int(input('Que ano quer analisar ? Coloque 0 para analisar o ano corrente! ').strip())
#if ano == 0:
#    ano = date.today().year
#if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#    print('O ano {} é BISSEXTO!'.format(ano))
#else:
#    print('O ano {} NÃO É BISSEXTO!'.format(ano))

#EXERCÍCIO 33
#a = float(input('Primeiro valor: '))
#b = float(input('Segundo valor: '))
#c = float(input('Terceiro valor: '))
#menor = a
#if b < a and b < c:
#    menor = b
#if c < a and c < b:
#    menor = c
#maior = a
#if b > a and b > c:
#    maior = b
#if c > a and c > b:
#    maior = c
#print('O menor número é {}'.format(menor))
#print('O maior número é {}'.format(maior))

#EXERCÍCIO 34
#s = float(input('Quanto você ganha ? ').strip())
#if s <= 1.250:
#    a = s*1.1
#    a1 = (s-a)*(-1)
#    print('O seu aumento foi de {} reais, logo seu salário passa a ser de {} reais'.format(a1, a))
#else:
#    a2 = s*1.15
#    a3 = (s-a2)*(-1)
#print('O seu aumento foi de {} reais, logo seu salário passa a ser de {} reais'.format(a3, a2))

#EXERCÍCIO 35
#r1 = float(input('Quanto mede a primeira reta ? ').strip())
#r2 = float(input('Quanto mede a segunda reta ? ').strip())
#r3 = float(input('Quanto mede a terceira reta ? ').strip())
#if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
#    print('As retas acima, podem formar um triângulo!')
#else:
#    print('As retas acima, não podem formar um triângulo!')

