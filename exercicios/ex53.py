primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + 10 * razao  # Fórmula para o décimo termo da PA

for c in range(primeiro, decimo, razao):  # Gera os termos da PA
    print(f'{c}', end=' -> ')
print('Acabou')