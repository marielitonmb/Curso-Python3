# Aula 16 - Tuplas

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Coxinha')  # pode criar tuplas sem os parenteses

print(lanche[:-2])
print(lanche[-2:])
print(lanche[2])
print(lanche[1:])
print(lanche[:2])
print('-----------')

print(sorted(lanche))  # coloca em ordem alfabetica
print('-----------')

for comida in lanche:
    print(f'Vou comer {comida}.')
print('-----------')

for cont in range(0, len(lanche)):
    print(f'Vontade de comer {lanche[cont]}. Pos{cont}')
print('-----------')

for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida}. Pos{pos}')
print('-----------')

a = 2, 5, 4
b= (5, 8, 1, 2)
c = a + b  # une duas tuplas
d = b + a
print(c)
print(d)
print(c + d)
print(c.count(5))  # conta quantas vezes o elemento aparece na tupla
print(d.index(2))  # mostra a posiçao do elemento (na primeira ocorrencia dele)
print('-----------')

pessoa = ('Marieliton', 33, 'M', 1.78)  # tuplas podem conter varios tipos de dados
#del(pessoa)  # apaga variaveis
print(pessoa)
