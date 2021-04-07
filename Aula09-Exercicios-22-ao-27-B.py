#REVISÃO EXERCÍCIOS 22 AO 27

#EXERCÍCIO 22
#nome = str(input('Diga seu nome completo: ')).strip().upper()
#print('O seu nome em maiúsculas é {}'.format(nome.upper()))
#print('O seu nome em minúsculas é {}'.format(nome.lower()))
#separa = nome.split()
#print('O seu primeiro nome é {} e possui {} letras'.format(separa[0], len(separa[0])))

#EXERCÍCIO 23
#n = int(input('Digite um número de 0 a 9999: '))
#u = n % 10
#d = n // 10 % 10
#c = n // 100 % 10
#m = n // 1000 % 10
#print('Unidade(s): {}'.format(u))
#print('Dezena(s): {}'.format(d))
#print('Centena(s): {}'.format(c))
#print('Milhar(es): {}'.format(m))

#EXERCÍCIO 24
#cid = str(input('Diga em que cidade você nasceu: ')).strip().upper()
#print(cid[:5] == 'SANTO')

#EXERCÍCIO 25
#nome = str(input('Diga o seu nome completo: ')).strip().upper()
#print('Seu nome possui Silva ? {}'.format('SILVA' in nome))

#EXERCÍCIO 26
#frase = str(input('Digite uma frase: ')).strip().upper()
#letra = str(input('Digite uma letra de A a Z: ')).strip().upper()
#print('A letra {} que você escolheu, apareceu {} vezes na frase'.format(letra, frase.count(letra)))
#print('A primeira vez em que a letra {} apareceu, foi na posição {}'.format(letra, frase.find(letra)+1))
#print('A última vez em que a letra {} apareceu, foi na posição {}'.format(letra, frase.rfind(letra)+1))

#EXERCÍCIO 27
#nome = str(input('Digite seu nome completo: ')).strip()
#print('Muito prazer em te conhecer {}!'.format(nome))
#n = nome.split()
#print('Seu primeiro nome é {}'.format(n[0]))
#print('Seu último nome é {}'.format(n[len(n)-1]))

