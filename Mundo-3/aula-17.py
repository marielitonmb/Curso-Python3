# Aula 17 - Listas (Parte 1)

num = [2, 4, 67, 0]
num[2] = 15
print(num)
num.append(87)  # p/ adicionar elementos numa lista
num.reverse()   # p/ inverter a ordem dos elementos
num.sort()  # p/ colocar em ordem crescente/alfabetica
print(num)
num.sort(reverse=True)  # p/ colocar em ordem inversa
num.insert(2, 1)  # adiciona o valor '1' na posiçao '2'
print(num)
print(f'A lista tem {len(num)} elementos')
num.reverse()
num.pop()  # elimina o ultimo elemento da lista
print(num)
num.pop(1)  # elimina o elemento da posiçao '1' da lista
print(num)
num.insert(2, 15)
print(num)
num.remove(15)  # elimina a primeira ocorrencia do elemento
print(num)

if 5 in num:  # p/ testar se um elemento esta numa lista
    num.remove(5)
else:
    print('Nao tem 5 na lista')

valores = [] # valores = list() p/ inicializar uma lista
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for v in valores:
    print(f'{v}...', end='')
print('\n')

for c, v in enumerate(valores):
    print(f'Na posiçao {c} ta o valor {v}')

a = [1, 2, 3, 4, 5]
b = a  # igualar listas cria uma dependencia entre elas, o que altera em uma, altera na outra
print(f'Lista a = {a}')
print(f'lista b = {b}')
b[2] = 8
print(f'Lista a = {a}')
print(f'lista b = {b}')
print()
c = a[:]  # isso faz uma copia de a p/ c sem criar uma dependencia
print(f'Lista a = {a}')
print(f'lista c = {c}')
c[3] = 26
print(f'Lista a = {a}')
print(f'lista c = {c}')
