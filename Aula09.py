#frase = 'Curso em Video Python'
#print(frase[9:21])
#Fatiamento - Selecionar uma cadeia de caracteres

#frase = 'Curso em Video Python'
#print(frase[9:21:2])
#Fatiamento - Selecionar cadeia de caracteres desde o 9, até o 21, pulando em 2 em 2 espaços.

#frase = 'Curso em Video Python'
#print(frase[:5])
#Fatiamento - Selecionar cadeia de caracteres, do início até o quinto caracteres, sempre que não definir o número
#do início do fatiamento, ele irá considerar o começo da string.

#frase = 'Curso em Video Python'
#print(frase[15:])
#Fatiamento - Selecionar cadeia de caracteres, iniciando no espaço 15, indo até o final da string.

#frase = 'Curso em Video Python'
#print(frase[9::3])
#Fatiamento - Irá iniciar no 9, vai até o final, pulando em 3 em 3 caracteres.

#ANÁLISE
#frase = 'Curso em Video Python'
#print(len(frase))
#ANÁLISE - Irá te dizer quantos micro espaços da memória, tem a string.

#frase = 'Curso em Video Python'
#print(frase.count('o'))
#ANÁLISE - Irá te dizer, quantos caracteres, do que você definiu, tem a string.

#frase = 'Curso em Video Python'
#print(frase.count('o', 0, 13))
#ANÁLISE - Irá te dizer, quantos caracteres, do que você definiu, tem a string, entre o espaço 0 e 13.
#Contagem já com fatiamento.

#frase = 'Curso em Video Python'
#print(frase.find('deo'))
#ANÁLISE - Irá te dizer, em que micro espaço se iniciou o caractere "DEO" que você definiu.

#frase.find('Android')
#Quando não possui a cadeia de caracteres, na "Frase" que você definiu, ele irá retornar -1, te informando
#que aquela cadeia não existe em sua frase.

#frase = 'Curso em Video Python'
#print('Curso' in frase)
#ANÁLISE - Função "IN", para verificar se determinada cadeia de caracteres existe em sua variável.
#Irá dar o valor False ou True.

#TRANSFORMAÇÃO
#frase = 'Curso em Video Python'
#print(frase.replace('Python', 'Android'))
#TRANSFORMAÇÃO - Posso alterar uma cadeia de caracteres da minha variável.

#frase.upper() - Irá deixar toda a cadeia de caracteres com letras maiúsculas.
#frase.lower() - Irá deixar toda a cadeia de caracteres com letras minúsculas.
#frase.capitalize() - Irá deixar todos caracteres em minúsculos, e apenas o primeiro caractere
#da cadeia, irá ficar em maiúscula.
#frase.title() - Irá deixar todo começo de string em letras maiúsculas.
#frase.strip() - Remover os espaços inúteis, no início e final da string.
#frase.rstrip() - Remover espaços inúteis, do lado direito.
#frase.lstrip() - Remover espaços inúteis, do lado esquerdo.


#DIVISÃO
#frase.split() - Irá fazer uma divisão entre os espaços.
#basicamente irá refazer os indices.

#JUNÇÃO
#'-'.join(frase) - Irá juntar as divisões, de elemtnos de frase, e gerar
#uma cadeia de string única, com hífen. pode alterar o hífen por espaço.

