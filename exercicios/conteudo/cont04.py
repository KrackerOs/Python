#import math 
#num1 = int(input('Digite um Numero: '))
#raiz = math.sqrt(num1)
#print('A raiz de {} é igual a {}'.format(num1, math.ceil(raiz))) #Ceil arredonda um numero para cima
#print('A raiz de {} é igual a {}'.format(num1, math.floor(raiz))) #floor arredonda a nota para um numero abaixo
 
#Importando funcionalidades especificas

from math import sqrt, floor, ceil 
num01 = int(input('Digite seu numero: '))
raiz = sqrt(num01)
print('A raiz de {} é igual a {}'.format(num01, ceil(raiz)))