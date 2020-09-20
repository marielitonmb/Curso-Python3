# Aula 13 - Desafio 46: Contagem regressiva
# Fazer uma uma contagem regressiva de 10 ate 0 com uma pausa de 1s entre os numeros

import time

for n in range(10, 0, -1):
    print(f'{n}... ', end='')
    time.sleep(1)
print('\n\033[1;30mFELIZ ANO NOVO!!!\033[m', '\033[1m\o/ \o|\033[m'*2)
