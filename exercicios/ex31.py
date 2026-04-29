v = float(input('A quantos km você estava?: '))

if v <= 80:
    print('Parabéns! você está dentro do limite de velocidade')
    
else: 
    print('Você foi multado por excesso de velocidade!')
    multa = (v - 80) * 7 
    print('A sua multa será de {}'.format(multa))