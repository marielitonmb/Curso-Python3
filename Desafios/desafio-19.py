# Aula 8 - Desafio 19: Sorteando um item na lista
# Ler 4 nomes e sortear um entre eles

import random

aluno = input('Informe o nome de 4 alunos: ').split()

print(f'O aluno escolhido para apagar o quadro foi {random.choice(aluno)}')
