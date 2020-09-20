# Aula 20 - Desafio 98: Funçao de contador
# Criar uma funçao chamada contador(), que receba tres parametros: inicio, fim e passo e realizar uma contagem.
# O programa tem que realizar tres contagens atraves da funçao criada:
# - de 1 ate 10, de 1 em 1
# - de 10 ate 0, de 2 em 2
# - uma contagem personalizada
# Obs: tem que fazer contagem regressiva tambem

from time import sleep

def crescente():
    for i in range(1, 11):
        print(f'{i} ', end='')
        sleep(0.5)
    print('FIM!\n')
    print('+='*20)

def decrescente():
    for i in range(10, -1, -2):
        print(f'{i} ', end='')
        sleep(0.5)
    print('FIM!\n')
    print('+=' * 20)

def contador():
    crescente()
    decrescente()
    print('Passe os parametros pra fazer a sua contagem:')
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))

    if passo == 0:
        passo = 1

    if inicio > fim:
        passo = -1

    for i in range(inicio, fim, passo):
        print(f'{i} ', end='')
        sleep(0.5)
    print('FIM!\n')
    print('+=' * 20)


contador()

# outra maneira
'''
def contador(i, f, p):
    if p < 0:
       p *= -1
    if p == 0:
       p = 1

    print('=+'*20)
    print(f'Contagem de {i} ate {f} de {p} em {p}:')
    sleep(1)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('=+'*20)
print('Passe os parametros pra fazer a sua contagem:')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
'''