from random import choice
aluno1 = str(input('Escreva o nome do primeiro aluno: '))
aluno2 = str(input('Escreva o nome do segundo aluno: '))
aluno3 = str(input('Escreva o nome do terceiro aluno: '))
lista = [aluno1, aluno2, aluno3]
escolha = choice(lista)
print('O escolhido para apagar o quadro foi {}'.format(escolha))