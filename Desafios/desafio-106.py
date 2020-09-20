# Aula 21 - Desafio 106: Interactive helping system in Python
# Fazer um mini-sistema que utilize o Interactive Help do Python.
# O usuario vai digitar o comando e o manual vai aparecer.
# Quando o usuario digitar 'FIM', o programa encerra.
# Obs: usar cores.

def pyHelp():
    from time import sleep

    while True:
        print('\033[1;7;32mSISTEMA DE AJUDA PyHELP')
        aux = input('\033[mFunçao ou Biblioteca > ').lower().strip()
        if aux == 'fim':
            print('FIM!')
            break
        else:
            print('\033[7;36m=+'*18)
            print(f'\033[7;36mAcessando o manual do comando "{aux}"')
            print('\033[7;36m=+'*18)
            sleep(2)
            print(f'\033[m')
            print(f'\033[7;37m')
            print(f'{help(aux)}')
            print(f'\033[m')
            sleep(3)


pyHelp()

# outra maneira
'''
from time import sleep
c = ('\033[m',         # 0 - sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;30m'      # 6 - branco
     );


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('='*tam)
    print(f' {msg}')
    print('='*tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Funçao ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO', 1)
'''