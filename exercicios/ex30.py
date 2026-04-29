import random

computador = random.randint(0, 5)


print("Estou pensando em um número entre 0 e 5...")
numero_usuario = int(input("Tente adivinhar qual número eu pensei: "))

if numero_usuario == computador:
    print("Parabéns! Você acertou! Eu realmente pensei no número {}.".format(computador))
else:
    print("Que pena! Você errou. Eu pensei no número {}.".format(computador))
    
