# Aula 18 - Desafio 85: Listas com pares e impares
# Ler 7 valores numericos e coloca-los numa lista unica que mantenha separados os valores pares e impares.
# No final, mostrar os valores pares e impares em ordem crescente.

numeros = []
par = []
impar = []

for n in range(1, 8):
    num = int(input(f'Digite o {n}º numero: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

par.sort()
impar.sort()
numeros = par[:], impar[:]

print('=+'*25)
print(f'Lista completa: {numeros}')
print(f'Numeros pares: {par}')
print(f'Numeros impares: {impar}')

# outra maneira
'''
num = [[], []]
valor = 0
for i in range(1, 8):
    valor = int(input(f'Digite o {i}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('=+'*20)
num[0].sort()
num[1].sort()
print(f'Os valores pares foram: {num[0]}')
print(f'Os valores impares foram: {num[1]}')
'''