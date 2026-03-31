import random
aluno1 = input('Escreva o nome do primeiro aluno: ')
aluno2 = input('Escreva o nome do segundo aluno: ')
aluno3 = input('Escreva o nome do terceiro aluno: ')
aluno4 = input('Escreva o nome do quarto aluno : ')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('Os 4 alunos escolhidos para apagar o quadro foram os: {}'.format(lista))