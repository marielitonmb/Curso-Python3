# Aula 13 - Desafio 54: Grupo da maioridade
# Ler o ano de nascimento de 7 pessoas. Depois informar quantas nao atingiram a maioridade (21) e quantas ja atingiram

from datetime import date

ano = date.today().year
jovem, adulto = 0, 0

for n in range(1, 8):
    nasc = int(input(f'Ano de nascimento da {n}ª pessoa: '))
    idade = ano - nasc
    if idade < 21:
        jovem += 1
    else:
        adulto += 1

print(f'Das 7 pessoas, {jovem} nao atingiram a maioridade e {adulto} ja.')
