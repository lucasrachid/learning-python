#EXERCÍCIO 29
carro = float(input('A Quantos KM por hora você está ? ').strip())
if carro >= 80.0:
    multa = (carro-80.0)*7
    print('Você foi multado em {} reais por ultrapassar o limite dessa via!'.format(multa))
else:
    print('Parabéns por respeitar as leis de Trânsito!')