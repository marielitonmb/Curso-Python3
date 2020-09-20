# Aula 22 - Desafio 111: Transformando modulos em pacotes
# Criar um pacote chamado utilidadesCeV que tenha dois modulos internos chamados moeda e dado.
# Transfira todas as funçoes utilizadas nos desafios 107, 108 e 109 para o primeiro pacote
# e mantenha tudo funcionando.

from desafio111.utilidadesCeV import moeda

p = float(input('Digite o preço:'))
moeda.resumo(p, 25, 15)
