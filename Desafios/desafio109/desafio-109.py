# Aula 22 - Desafio 109: Formatando moedas em Python v2.0
# Modificar as funçoes que foram criadas no desafio 107 para que elas aceitem um parametro a mais,
# informando se o valor retornado por elas vai ser ou nao formatado pela funçao moeda(),
# desenvolvido no desafio 108.

from desafio109 import moeda

p = float(input('Digite o preço:'))
print(f'A metade de {moeda.moeda(p)} eh {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} eh {moeda.dobro(p)}')
print(f'Aumentando 20%, temos {moeda.aumentar(p, 20, True)}')
print(f'Reduzindo 15%, temos {moeda.diminuir(p, 15)}')
