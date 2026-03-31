from math import sqrt
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
cm = (ca**2 + co**2)*0.5
print('O resultado do cateto oposto com cateto adjacente é {}'.format(cm))