# Aula 5 - Desafio 2: Respondendo ao usuario

nome = input('Digite seu nome: ')

ciano = '\033[36m'
limpa = '\033[m'

print(f'Seu nome é, {ciano}{nome}{limpa}!')
