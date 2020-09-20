# Aula 7 - Operadores Aritméticos

# -*- coding: utf-8 -*-
# -*- coding: cp1252 -*

'''
nome = input('Qual o seu nome? ')
print(f'Prazer em conhecer voce, {nome}')
print('='*20)
'''

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print(f'A soma eh {a} e a subtraçao eh {s}', end=' ') # esse end=' ' emenda os prints numa unica linha
print(f'A multiplicaçao eh {m} e a divisao eh {d:.2f}')
print(f'A divisao inteira eh {di} e n1 elevado a n2 eh igual a {e}')



