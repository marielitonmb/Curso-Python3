# Aula 8 - Utilizando Módulos

from math import sqrt, floor
import emoji

num = int(input('Digite um numero: '))

raiz = sqrt(num)  # importando apenas um modulo da biblioteca, nao eh necessario declarar a biblioteca (math.sqrt)

print(f'A raiz quadrada de {num} eh {floor(raiz):.2f}')  # floor() arredonda pra cima

print(emoji.emojize('Teste da biblioteca emoji :sunglasses:', use_aliases=True))
