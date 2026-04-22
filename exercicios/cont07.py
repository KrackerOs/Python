frase = '       curso de analise de desenvolvimento de sistemas'
print(frase[40]) #Isso mostra o espaço na memória
print(frase[40:44]) #É um intervalo de caracteres, menos o ultimo
print(frase[40:44:2])#Coloando o 2, pulamos em 2 em dois em dois
print(frase[:2])#Como foi 2, pegou somente os primeiros 2 caracteres
print(frase[2:])#Pegou o numero de caracteres que eu escolhi até o final
print(frase[5::2])#Pegou do numero de caracteres que eu escolhi pulando 2 casas, já que o numero colocado ali foi 2
print(len(frase))#Esse método conta a quantidade caracteres
print(frase.count('a', 1,10))#Ele procurou quantas letras a do numero de caractere escolhido até o maxímo de 10 caracteres
print(frase.find('Curso'))#O Find mostra apartir de qual indice mostra a pesquisa, tipo curso começa com 0, já que o primeiro caractere é sempre 0(
print(frase.find('android'))#O resultado -1 significa que não há essa sequencia de caracteres na frase 
print('seila'in frase)#O 'in' verifica se esse conjunto de frase está na variavel, dando um valor booleano, ou seja true (verdadeiro), ou false (Falso)
print(frase.replace('Curso', 'seila'))#troca as frasses
print(frase)
print(frase.upper())#Upper deixa todas as letras maiusculas
print(frase.lower())#lower deixa todas as letras que já estão em maiusculas em minusculas
print(frase.capitalize())#Deixa a primeira palavra em maiusculo
print(frase.title())#deixa todas as letras depois do espaço vazio(espaço) em maiusculo
print(frase.strip())#O strip tira o espaço em branco do inicio e do final
print(frase.rstrip())#O rstrip tira o espaço em branco da direita
print(frase.lstrip())#O lstrip tira o espaço em branco da esquerda
print(frase.split())
print('*'.join(frase))#No join, você une o simbolo digitado em cada parte do split