n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
d = n1/n2
sub = n1-n2
pot = n1**n2
rest = n1%n2
mult = n1*n2
divi = n1//n2
# print('O resultado da multiplicação é: {}'.format(mult), =end=' ') - Dessa forma, o print não quebra linha
# print('O resultado do cálculo é: {}'.format(mult, s, d)) (contra barra"n") - você quebra linha
# print('O resultado da potência é: {}'.format(pot))
# print('O resultado da Divisão inteira é: {}'.format(divi))
print('O resultado da soma é: {}, da divisão é: {:.3f} e da multiplicação é: {}'.format(s, d, mult))