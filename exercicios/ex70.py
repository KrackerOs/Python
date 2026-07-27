from random import randint

print('Vamos jogar par ou ímpar!')
cont = 0

while True:
    palpite = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? ')).strip().lower()
    pc = randint(1, 10)
    resultado = palpite + pc

    if (resultado % 2 == 0 and escolha == 'par') or (resultado % 2 != 0 and escolha == 'impar'):
        print(f'Você jogou {palpite} e o computador jogou {pc}. Total de {resultado} deu {escolha}.')
        cont += 1
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
    else:
        escolhapc = 'par' if resultado % 2 == 0 else 'impar'
        print(f'Você jogou {palpite} e o computador jogou {pc}. Total de {resultado} deu {escolhapc}.')
        print('Você PERDEU!')
        break

print(f'Game Over! Você venceu {cont} vezes.')