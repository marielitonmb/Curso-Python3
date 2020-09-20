# Aula 22 - Desafio 107: Exercitando modulos em Python
# Criar um modulo chamado moeda.py que tenha as funçoes:
# aumentar(), diminuir(), dobro() e metade().
# Fazer um programa que importe esse modulo e use algumas dessas funçoes.
# Obs: Crie um pasta chamada desafio107 e faça o mesmo pra os demais desafios.

from desafio107 import moeda

p = float(input('Digite um preço R$:'))

print(f'A metade de {p} eh {moeda.metade(p)}')
print(f'O dobro de {p} eh {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')
