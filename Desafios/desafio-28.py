# Aula 10 - Desafio 28: Jogo da advinhaçao v1.0

import random

num = int(input('Digite um numero entre 1 e 10: '))

num_pc = random.randint(1, 10)

if num == num_pc:
    print(f'O numero que voce digitou ({num}) foi igual ao sorteado ({num_pc})')
else:
    print(f'O seu numero ({num}) foi diferente do sorteado ({num_pc})')
