# Aula 14 - Desafio 60: Calculo do fatorial
# Ler um numero e calcular o seu fatorial.
# 5! = 1*2*3*4*5 = 120

fat = 1
while True:
    f = int(input('Digite um numero pra saber o seu fatorial: '))
    print(f'\033[1m{f}!\033[m => ', end='')
    for n in range(1, f + 1):
        fat = fat * ((n - 1) + 1)
        print(f'{((n - 1) + 1)}', end='')
        print(' * ' if n < f else '', end='')
    print(f' => \033[1m{fat}\033[m')
    fat = 1
    print()

# outra maneira 1
'''
from math import factorial
n = int(input('Digite um numero para saber o seu fatorial: '))
f = factorial(n)
print(f'{n}! = {f}')
'''
# outra maneira 2
'''
n = int(input('Digite um numero para saber o seu fatorial: '))
c = n
f = 1  # sempre inicializar variaveis p/ multiplicaçao com '1'
print(f'{n}! = ', end='')
while c > 0:
    print(f'{c} ', end='')
    print('x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print(f)
'''
