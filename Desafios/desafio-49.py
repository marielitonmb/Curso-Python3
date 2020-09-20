# Aula 13 - Desafio 49: Tabuada v2.0
# Refazer o desafio-09 usando o laço for

n = int(input('Digite um numero: '))

print('='*5, f'\033[4mTabuada de adiçao\033[m', '='*5)
for num in range(1, 11):
    print(' '*5, f'{n} + {num:2} = {n+num:2}')
print()

print('='*5, f'\033[4mTabuada de subtraçao\033[m', '='*5)
for num in range(1, 11):
    print(' '*5, f'{n} - {num:2} = {n-num:2}')
print()

print('='*5, f'\033[4mTabuada de multiplicaçao\033[m', '='*5)
for num in range(1, 11):
    print(' '*5, f'{n} * {num:2} = {n*num:2}')
print()

print('='*5, f'\033[4mTabuada de divisao\033[m', '='*5)
for num in range(1, 11):
    print(' '*5, f'{n} / {num:2} = {n/num:.2f}')
