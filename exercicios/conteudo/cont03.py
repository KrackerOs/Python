seila = input('Qual seu nome?: ')
print('Prazer em te conhecer {:20}!'.format(seila)) #O 20 faz o "!" ficar 20 espaços a frente
print('Prazer em te conhecer {:<20}!'.format(seila)) #O sinal de maior faz ele ir para a esquerda
print('Prazer em te conhecer {:>20}!'.format(seila)) #O sinal de menor faz ele ir para a direita
print('Prazer em te conhecer {:^20}!'.format(seila)) #O sinal circunflexo faz ele ficar alinhado no centro

ka = int(input('Digite um valor: '))
ke = int(input('Digite outro valor: '))
ki = ka+ke
print('O primeiro valor de {} + o valor de {} somado da {}'.format(ka, ke, ki))