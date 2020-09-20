# Aula 20 - Desafio 99: Funçao que descobre o maior
# Criar uma funçao chamada maior(), que receba varios parametros com valores inteiros.
# O programa tem que analisar todos os valores e dizer qual deles eh o maior.

from time import sleep

def maior(* num):
    quant = len(num)
    resp = max(num)
    print('Analisando os valores informados...')
    sleep(1)
    print(f'Foram informados \033[1;31m{quant}\033[m valores, sao eles: ', end='')
    for i in num:
        print(f'\033[1;32m{i}\033[m', end=' ')
        sleep(0.5)
    print(f'\nO maior entre eles foi \033[1;33m{resp}\033[m')
    print('-'*40)


maior(4, 8, 42, -9, 7)
maior(-6, -1)
maior(5, 3, 7)
