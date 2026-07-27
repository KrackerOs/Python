maior = homens = mulheres = 0

while True:
    print('---' * 10)
    print('CADASTRE UMA PESSOA: ')
    print('---' * 10)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().lower()[0]
    continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]

    if idade > 18:
        maior += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulheres += 1
    if continuar == 'n':
        break

print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')