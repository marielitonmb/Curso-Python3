# Aula 17 - Desafio 79: Valores unicos em uma lista
# Ler varios numeros e coloca-los numa lista, caso um numero ja exista na lista, ele nao eh adicionado.
# No final, mostrar todos os valores unicos lidos em ordem crescente.

lista = []

while True:
    num = int(input('Digite um numero: '))
    if num in lista:
        print(f'{num} ja foi registrado, informe outro numero.')
    else:
        lista.append(num)
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if continua == 'N':
        break
    elif continua == 'S':
        pass

lista.sort()
print('-'*30)
print(f'Lista final em ordem crescente:')
print(f'{lista}')
