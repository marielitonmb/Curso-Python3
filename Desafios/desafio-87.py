# Aula 18 - Desafio 87: Mais sobre matriz em Python
# Aprimorar o desafio anterior:
# - somar todos os valores pares digitados
# - a soma dos valores da terceira coluna
# - o maior valor da segunda linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = scol = maior = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor p/ a posiçao ({linha},{coluna}): '))

print('='*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')  # O '^5' usa 5 espaços e centraliza
        if matriz[linha][coluna] % 2 == 0:
            spar += matriz[linha][coluna]
    print()

print('='*30)
print(f'A soma dos numeros pares eh {spar}')
for linha in range(0, 3):
    scol += matriz[linha][2]
print(f'A soma dos elementos da 3ª coluna eh {scol}')
for coluna in range(0, 3):
    if matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor da 2ª linha eh {maior}')
