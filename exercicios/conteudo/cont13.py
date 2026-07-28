# Tuplas(variáveis compostas)
# Relembrando do primeiro trimestre, toda vez que um variável simples é declarada um espaço na memória e criado no computador. Onde valores são guardados pelo operador de . Em variáveis simples se eu quiser guardar mais um valor dentro do espaço criado na memória o que estava armazenado anteriormente é excluido e o novo valor é armazenado. Para resolvermos esse problema podemos criar mais espaços na memória em uma mesma variável, e uma dessas formas e com o uso de tuplas. Os elementos de uma tupla pode ser selecionados através de seus índices que inicia-se no valor 0

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])#Vai apartir do 2 indice até o final
print(lanche[:2]) #começa do começo até o segundo indice, desconsiderando ele
print(lanche[::-1])