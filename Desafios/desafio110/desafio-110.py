# Aula 22 - Desafio 110: Reduzindo ainda mais o seu programa
# Adicionar ao modulo moeda.py, criado nos desadios anteriores, uma funçao
# chamada resumo(), que mostre na tela algumas informaçoes geradas pelas
# funçoes que ja existem no modulo.

from desafio110 import moeda

p = float(input('Digite o preço:'))
moeda.resumo(p, 80, 35)
