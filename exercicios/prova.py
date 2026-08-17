import random
while True:
    eu = int(input('Escolha um numero de 0 a 9: '))
    computador = random.randint(0, 9)
    if eu == computador:
        print('Bom, parece que você ganhou, parabéns!')
        break
    else: 
        print('Hahaha, eu ganhei!')