sexo = str(input('Informe seus dados [M/F]: ')).strip().lower()[0]
while sexo not in 'mf':
    sexo = str(input('Dados inconsistentes. Informe novamente [M/F]: ')).strip().lower()[0]
print(f'O seu sexo é {sexo.upper()}')