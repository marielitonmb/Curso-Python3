# Aula 6 - Tipos Primitivos e Saída de Dados

# -*- coding: utf-8 -*-

n = input('Digite algo: ')

print('Isso que foi digitado eh do tipo', type(n))
print('Eh numero? ', n.isnumeric())
print('Eh alfabetico? ', n.isalpha())
print('Eh alfanumerico? ', n.isalnum())
print('Eh imprimivel? ', n.isprintable())
print('Eh ASCII? ', n.isascii())
print('Eh tudo minusculo? ', n.islower())
print('Eh tudo maiusculo? ', n.isupper())
print('Soh tem espaços? ', n.isspace())
print('Eh capitalizada (maiusc e minusc)? ', n.istitle())

# A partir do python 3.7, o .animformat() ficou assim:
print(f'O tipo primitivo desse valor é {type(n)}')
