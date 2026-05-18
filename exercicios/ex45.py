# Entrada de peso e altura
peso = float(input("Qual é o seu peso? (kg) "))
altura = float(input("Qual é a sua altura? (m) "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Exibição do IMC
print("O IMC dessa pessoa é de {:.1f}".format(imc))

# Verificação das categorias de IMC
if imc < 18.5:
    print("Você está abaixo do peso normal")
elif 18.5 <= imc < 25:
    print("Parabéns, você está no peso ideal")
elif 25 <= imc < 30:
    print("Você está em sobrepeso")
elif 30 <= imc < 40:
    print("Você está com obesidade, cuidado")
else:
    print("Você está em obesidade mórbida, cuidado")