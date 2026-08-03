n = c = s = 0 
while True:
    n = int(input('Digite um número (757 para parar): '))
    c += 1 
    s += n
    if n == 757:  
        break
    multip = c*s 
print(f'A quantidade de numeros de digitados foram {c} e a multiplicação dos numeros foi {multip}, já multiplicando o flag deu {c * s} !')

