nota1 = float(input('Qual é a primeira nota do aluno?: '))
nota2 = float(input('Qual é a segunda nota do aluno?: '))
media = (nota1 + nota2) / 2
if media <5:
    print('O aluno foi reprovado')
    
elif media >=5 and media <=6.9:
    print('O aluno está de recuperação')
    
else:
    print('O aluno foi aprovado')