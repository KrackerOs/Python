#c = 1
#while c < 10: 
    #print(c)
#c +=  1 #Isso significa que o c vai aumentar de 1 em 1 até chegar no limite que é 9
#O while serve para quando sabemos ou não o limite

# n = 1
# while n != 0:
#    n=int(input('Digite um valor: '))
# print('Fim do programa!')

# r = 'sim'
# while r == 'sim':
#     n = int(input('Digite um valor: '))
#     r = str(input('Quer continuar? [Sim/Não]: ')).lower()

n = 1 
par = 0
impar = 0
while n != 0: 
    n = int(input('Digite um valor: '))
    if n !=0:
        if n % 2 == 0: 
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} numeros pares e {impar} numeros impares ')