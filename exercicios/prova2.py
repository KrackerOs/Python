from time import sleep
import random


tentativa1 = int(input('''Jokenpô:
[1] Pedra
[2] Papel
[3] Tesoura
Escolha: '''))

maquina = random.randint(1, 3)


opcoes = {1: "Pedra", 2: "Papel", 3: "Tesoura"}
if tentativa1 in opcoes:
    print(f"Você escolheu: {opcoes[tentativa1]}")
    print(f"A máquina escolheu: {opcoes[maquina]}")

   
    print('Jo')
    sleep(1)
    print('ken')
    sleep(1)
    print('pô')
    sleep(1)


    if tentativa1 == 1 and maquina == 2:
        print('Você perdeu!')
    elif tentativa1 == 1 and maquina == 3:
        print('Você ganhou!')
    elif tentativa1 == 1 and maquina == 1:
        print('Empatou!')

    elif tentativa1 == 2 and maquina == 1:
        print('Você ganhou!')
    elif tentativa1 == 2 and maquina == 3:
        print('Você perdeu!')
    elif tentativa1 == 2 and maquina == 2:
        print('Empatou!')

    elif tentativa1 == 3 and maquina == 1:
        print('Você perdeu!')
    elif tentativa1 == 3 and maquina == 2:
        print('Você ganhou!')
    elif tentativa1 == 3 and maquina == 3:
        print('Empatou!')
else:
    print("Opção inválida! Escolha entre 1, 2 ou 3.")