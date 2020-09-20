# Aula 18 - Desafio 86: Matriz em Python
# Criar uma matriz 3x3 e preencher com valores lidos pelo teclado. (tudo numa unica lista)
# No final, a matriz na tela, com a formataçao correta.
'''
00 01 02
10 11 12
20 21 22
'''

matriz = []
coordenadas = []
for a in range(3):
    for b in range(3):
        coordenadas.append(int(input(f'Informe o dado da coordenada ({a},{b}): ')))
        matriz.append(coordenadas[:])
        coordenadas.clear()

titulo = ' MATRIZ 3X3 '
print('=+'*10)
print(titulo.center(20, '#'))
print('=+'*10)

for c in range(3):
    print(matriz[c], end=' ')
print()
for c in range(3, 6):
    print(matriz[c], end=' ')
print()
for c in range(6, 9):
    print(matriz[c], end=' ')

# outra maneira
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor p/ a posiçao ({linha},{coluna}): '))

print('='*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')  # O '^5' usa 5 espaços e centraliza
    print()
'''