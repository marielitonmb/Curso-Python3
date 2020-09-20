# Aula 16 - Desafio 74: Maior e menor valores em tuplas
# Gerar de forma aleatoria 5 numeros e coloca-los numa tupla.
# Depois mostrar a listagem dos numeros gerados e indicar o maior e o menor dentro da tupla.

from random import randint

numeros = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print(f'Numeros gerados = {numeros}')
print(f'Maior numero da tupla = {max(numeros)}')
print(f'Menor numero da tupla = {min(numeros)}')

# pra mostrar os numeros fora dos parenteses
#print('Numeros gerados: ', end='')
#for n in numeros:
#    print(f'{n}', end='')
