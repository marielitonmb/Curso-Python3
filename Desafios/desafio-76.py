# Aula 16 - Desafio 76: Lista de preços com tupla
# Criar uma tupla unica com nomes de produtos e seus respectivos preços na sequencia.
# No final, mostrar uma listagem de preços, organizando os dados em forma tabular.

tupla = ('Pao', 2, 'Leite', 3.5, 'Bicoito', 1.10, 'Tareco', 4, 'Detergente', 3.20)

print('='*40)
print(f'{"LISTA DE PRODUTOS":^40}')  # centraliza
print('='*40)
for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<32}', end='')  # alinha p/ esquerda
    else:
        print(f'R${tupla[pos]:>5.2f}')  # alinha p/ direita
print('-'*40)

'''
print('\033[4mItem\033[m ........................... \033[4mPreço\033[m')
print(f'{tupla[0]} ............................ R$ {tupla[1]}')
print(f'{tupla[2]} .......................... R$ {tupla[3]}')
print(f'{tupla[4]} ........................ R$ {tupla[5]}')
print(f'{tupla[6]} ......................... R$ {tupla[7]}')
print(f'{tupla[8]} ..................... R$ {tupla[9]}')
'''
