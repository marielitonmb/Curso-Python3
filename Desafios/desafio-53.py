# Aula 13 - Desafio 53: Detector de palindromo
# Ler uma frase qualquer e dizer se eh um palindromo, desconsiderando os espaços
# Ex: "apos a sopa", "a sacada da casa", "a torre da derrota", "o lobo ama o bolo"

frase = input('Digite uma frase: ').lower().strip()
frase = frase.replace(' ', '')
frase_inv = frase[::-1]

if frase == frase_inv:
    print(f'{frase} eh igual a {frase_inv}')
    print('Logo \033[1;4mSIM\033[m, eh um palindromo!')
else:
    print(f'{frase} eh diferente de {frase_inv}')
    print('Logo \033[1;4mNAO EH\033[m um palindromo!')

'''
### outra maneira ###

frase = input('Digite uma frase: ').lower().strip()
palavras = frase.split()
juntar = ''.join(palavras)
inverter = ''

for letra in range(len(juntar) - 1, -1, -1):
    inverter += juntar[letra]

print(f'O inverso de {juntar} eh {inverter}.')
if juntar == inverter:
    print('Temos um palindromo!')
else:
    print('A frase digitada nao eh um palindromo!')
'''