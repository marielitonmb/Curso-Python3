# Aula 11 - Cores no Terminal

print('\033[7;30mTeste\033[m')

a = 'azul'
b = 'verde'
c = 'vermelho'
d = 'roxo'

print(f'As cores sao \033[1;34m{a}, \033[32m{b}, \033[31m{c}\033[m e \033[35m{d}')

print(f'\033[1;31;42m1 2 3 4 5 6\033[m')

print('\033[1;32mVERDE\033[m \033[1;33mAMARELO\033[m')

ciano = '\033[36m'
limpa = '\033[m'

print(f'{ciano}{c}{limpa}')