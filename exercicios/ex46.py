from time import sleep

produto = float(input('Qual é o preço do produto? R$: '))

print('----Carregando forma de pagamento----')
sleep(3)

fp = str(input('''Qual será a sua forma de pagamento? 
               [1] A vista dinheiro/cheque
               [2] A vista no cartão(5 % de desconto)
               [3] EM até 2x no cartão (Preço normal)
               [4] Em até 3x no cartão(20% de juros)'''))

if  fp == 1:
    desconto = produt0 - (produto*0.10)
    print(f'Sua compra com desconto fica R${desconto}')
elif fp == 2:
    cartao = produto - (produto*0.05)
    print(f'Sua compra no cartão com desconto de 5% fica em R$:{cartao}')
elif fp == 3:
    em2x = produto/2
    