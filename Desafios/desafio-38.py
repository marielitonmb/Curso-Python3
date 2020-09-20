# Aula 12 - Desafio 38: Comparando numeros
# Leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
# "O primeiro valor eh maior"
# "O segundo valor eh maior"
# "Nao existe valor maior. Os dois sao iguais"

n1 = int(input('Digite o 1º numero: '))
n2 = int(input('Digite o 2º numero: '))

if n1 > n2:
    print('O primeiro valor', n1, 'eh o maior.')
elif n1 < n2:
    print('O segundo valor', n2, 'eh o maior.')
else:
    print('Nao existe valor maior. Os dois numeros informados sao iguais!')
