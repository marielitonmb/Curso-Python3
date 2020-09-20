# Aula 19 - Desafio 91: Jogo de dados em Python
# Programa em que 4 jogadores joguem um dado e tenham resultados aleatorios.
# Guardar esses resultados num dicionario.
# No final, colocar o dicionario em ordem, sabendo que o vencedor tirou o maior numero do dado.
# Obs: cada jogador eh uma key do dicionario e o valor eh o numero sorteado.
'''
Valores sorteados: # use o sleep() entre os prints
    o jagador1 tirou 5
    o jagador2 tirou 2
    o jagador3 tirou 6
    o jagador4 tirou 1
Ranking dos jogadores:
    1º lugar: jogador3 com 6
    2º lugar: jogador1 com 5
    3º lugar: jogador2 com 2
    4º lugar: jogador4 com 1
'''

import operator  # p/ usar o sorted no dicionario
from random import randint
from time import sleep

jogo = dict()
jogo['jogador1'] = randint(1, 6)
jogo['jogador2'] = randint(1, 6)
jogo['jogador3'] = randint(1, 6)
jogo['jogador4'] = randint(1, 6)

print('Os valores sorteado foram:')
sleep(1)
for key, valor in jogo.items():
    print(f'O {key} tirou {valor}')
    sleep(1)

# O jogo.items devolve o par de elementos do dicionário de valor chave.
# key=operator.itemgetter(1) especifica que a chave de comparação é o valor do dicionário,
# enquanto que operator.itemgetter(0) usa a propria chave como comparação.
ranking = sorted(jogo.items(), key=operator.itemgetter(1))  # aqui vira uma lista ordenada
ranking.reverse()  # inverte a lista do maior pra o menor

print('='*20)
print('Ranking dos jogadores:')
sleep(1)
for i in range(0, 4):
    print(f'{i+1}º lugar: {ranking[i][0]} com {ranking[i][1]}')
    sleep(1)

# outra maneira
'''
from operator import itemgetter
from random import randint
from time import sleep

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

print('Valores sorteados:')
sleep(1)
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
    
ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-='*20)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
'''