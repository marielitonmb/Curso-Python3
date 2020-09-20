# Aula 10 - Desafio 33: Maior e menor valores
# Ler 3 numeros dizer qual é o maior e qual o menor entre eles

num1 = int(input('Valor 1: '))
num2 = int(input('Valor 2: '))
num3 = int(input('Valor 3: '))

maior, menor = num1, num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

print(f'O maior eh {maior}')

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print(f'O menor eh {menor}')

'''# Outro jeito de fazer

lista = [num1, num2, num3]

print(f'O menor numero é \033[34m{min(lista)}\033[m e o maior é \033[34m{max(lista)}\033[m')'''

