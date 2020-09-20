# Aula 10 - Desafio 32: Ano bissexto
# Ler um ano e informar se ele é bissexto ou não

from datetime import date

ano = int(input('Informe um ano para analisar (digite "0" para analisar o ano atual): '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} EH ano bissexto!')
else:
    print(f'{ano} NAO EH ano bissexto!')
