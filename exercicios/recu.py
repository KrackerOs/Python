import random
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
lista = [aluno1, aluno2, aluno3]
escolhido = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))