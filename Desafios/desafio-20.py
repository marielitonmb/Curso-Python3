# Aula 8 - Desafio 20: Sorteando uma ordem na lista
# Ler o nome de 4 alunos e apos um sorteio mostrar a ordemm de apresentação de cada um

from random import shuffle

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

lista = [a1, a2, a3, a4]
shuffle(lista)

print(f'A ordem de se apresentar sera {lista}')
