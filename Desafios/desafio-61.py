# Aula 14 - Desafio 61: Progressao aritmetica v2.0
# Refazer o desafio 51 usando while.

loop = True
while loop:
    primeiro = int(input('Informe o primeiro valor da PA: '))
    razao = int(input('Informe a razao da PA: '))
    decimo = primeiro + (10 - 1) * razao
    print('PA = ', end='')
    for c in range(primeiro, decimo + razao, razao):
        print(f'{c} -> ', end='')
    loop = False
print('FIM!')

# outra maneira
'''
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('FIM!')
'''
