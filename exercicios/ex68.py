n = c = 0 
q = 0
multip = 1
flag = 757
while True:
    n = int(input('Digite um número (757 para parar): '))
    
    if n == 757:
        multip *= n
        q += 1
        break
    multip *= n
    q += 1
print(f'A quantidade de numeros digitados foram {q}')
print(f'A multiplicação de todos incluindo o flag deu {multip}')
