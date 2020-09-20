# Aula 14 - Desafio 65: Maior e menor valores
# Ler varios numeros inteiros. No final, mostrar a media, o maior e o menor entre todos os valores.
# O programa deve perguntar ao usuario se ele quer continuar a digitar valores.

loop = True
soma, cont, maior, menor = 0, 0, 0, 9999999
while loop:
    num = int(input('Digite um numero: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
    cont += 1
    if cont % 5 == 0:
        opcao = input(f'Voce adiciou {cont} numeros, deseja continuar [S/N]? ').strip().lower()
        if opcao == 's':
            loop = True
        elif opcao == 'n':
            loop = False
        else:
            print('Opçao Invalida!')
            loop = False

print(f'Media dos valores digitados = \033[1;31m{soma/cont:.2f}\033[m')
print(f'Maior numero digitado = \033[1;31m{maior}\033[m')
print(f'Menor numero digitado = \033[1;31m{menor}\033[m')

# outra maneira
'''
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
media = soma / quant
print(f'Foram digitados {quant} numeros, e a media foi {media:.2f}.')
print(f'O maior numero foi {maior} e o menor foi {menor}.')
'''