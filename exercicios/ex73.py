print('='*30)
print('BANCO CEV')
print('='*30)

valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 100
totalced = 0

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totalced = 0
        if total == 0:
            break

print('='*30)
print('VOLTE SEMPRE')
