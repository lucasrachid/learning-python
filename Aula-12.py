nome = str(input('Qual é o seu nome ? ')).strip().upper()
if nome == 'LUCAS':
    print('Muito prazer Lucas, que belo nome!')
elif nome == 'MAX':
    print('Satisfação aspira!')
else:
    print('Muito prazer {}'.format(nome.capitalize()))
print('Tenha um bom dia!')