# Aula 8 - Desafio 18: Seno, cosseno e tangente
# Ler um angulo qualquer e calcular seu seno, cosseno e tangente

import math

angulo = int(input('Informe um angulo: '))

print(f'Seno de {angulo}º = {math.sin(angulo):.2f}'
      f'\nCosseno de {angulo}º = {math.cos(angulo):.2f}'
      f'\nTangente de {angulo}º = {math.tan(angulo):.2f}')
