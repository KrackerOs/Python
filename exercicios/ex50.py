s = 0
cont = 0
for c in range(1, 501, 2):  # Percorre os números ímpares de 1 a 500
    if c % 3 == 0:  # Verifica se o número é múltiplo de 3
        cont += 1  # Conta as repetições
        s += c  # Soma os valores

print(f"A soma de todos os {cont} valores solicitados é {s}")