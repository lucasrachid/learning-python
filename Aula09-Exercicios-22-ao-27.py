#EXERCÍCIO 22
#nome = str(input('Digite o seu nome completo: ')).strip()
#print('Analisando o seu nome...')
#print('Seu nome em maiúsculas é {}'.format(nome.upper()))
#print('Seu nome em minúsculas é {}'.format(nome.lower()))
#print('Seu nome tem ao todo {}'.format(len(nome)-nome.count(' ')))
##print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
#separa = nome.split()
#print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


#EXERCÍCIO 23
#num = int(input('Diga um número de 0 a 9999: '))
#u = num // 1 % 10
#d = num // 10 % 10
#c = num // 100 % 10
#m = num // 1000 % 10
#print('Analisando o número {}'.format(num))
#print('Unidades: {}\nDezenas: {}\nCentenas: {}\nMilhares: {}'.format(u, d, c, m))

#EXERCÍCIO 24
#city = str(input('Diga o nome de sua cidade: ')).strip()
#print(city[:5].upper() == 'SANTO')

#EXERCÍCIO 25
#nome = str(input('Diga o seu nome completo: ').split())
#print('Seu nome tem Silva ? {}'.format('SILVA' in nome.upper()))

#EXERCÍCIO 26
#frase = str(input('Digite uma frase: ').strip()).upper()
#print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
#print('A letra A apareceu a 1º vez na posição {}'.format(frase.find('A')+1))
#print('A letra A apareceu a última vez na posição {}'.format(frase.rfind('A')+1))

#EXERCÍCIO 27
#n = str(input('Digite o seu nome completo: ')).strip()
#print('Muito prazer em te conhecer {}!'.format(n))
#nome = n.split()
#print('Seu primeiro nome é {}'.format(nome[0]))
#print('Seu último nome é {}'.format(nome[len(nome)-1]))