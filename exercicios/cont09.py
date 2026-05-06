#Condições aninhadas
#São condições colocadas dentro de outras condições. Em condições aninhadas eu utilizo o se não se, dentro do se. Em python o #se não se é representado por elif condição: A partir do primeiro elif para mais condições você vai colocando um elif para cada #condição. Sempre que for usar o primiero elif tem que usar um if antes e o else se torna opcional.
nome = str(input('Qual é o seu nome?: '))
if nome == 'Kleber':
    print('Que nome lindo você tem!')
elif nome == 'Paulo' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')


