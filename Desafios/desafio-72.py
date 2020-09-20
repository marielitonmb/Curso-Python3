# Aula 16 - Desafio 72: Numero por extenso
# Escrever uma tupla com a contagem de zero a vinte escrito por extenso.
# O programa deve ler um numero do teclado entre 0 e 20 e mostrar ele por extenso.

tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if num not in range(0, 21):
        print('Numero fora da faixa!')
    else:
        print(f'\033[1m{num}\033[m por extenso eh \033[1;4m{tupla[num]}\033[m')
