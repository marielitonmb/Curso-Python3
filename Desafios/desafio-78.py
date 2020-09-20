# Aula 17 - Desafio 78: Maior e menor valores na lista
# Ler 5 numeros e guardar eles numa lista.
# No final, mostrar qual foi o maior e o menor valor e suas posiçoes na lista.

lista_num = []
for n in range(0, 5):
    lista_num.append(int(input(f'Digite um numero p/ a posiçao {n}: ')))

print('-='*30)
print(f'O maior numero digitado foi {max(lista_num)} e ele ta na posiçao {lista_num.index(max(lista_num))}.')
print(f'O menor numero digitado foi {min(lista_num)} e ele ta na posiçao {lista_num.index(min(lista_num))}.')

# outra maneira
'''
listanum = list()
maior = menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um numero p/ a posiçao {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        elif listanum[c] < menor:
            menor = listanum[c]

print('=*'*30)
print(f'O maior numero digitado foi {maior} na(s) posiçao(oes) ', end='')
for indice, valor in enumerate(listanum):
    if valor == maior:
        print(f'{indice}, ', end='')
print()
print(f'O menor numero digitado foi {menor} na(s) posiçao(oes) ', end='')
for indice, valor in enumerate(listanum):
    if valor == menor:
        print(f'{indice}, ', end='')
print()
'''