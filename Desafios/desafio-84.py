# Aula 18 - Desafio 84: Lista composta e analise de dados
# Ler o nome e o peso de varias pessoas guardando tudo numa lista. Depois mostrar:
# - quantas pessoas foram cadastradas
# - uma listagem com as pessoas mais pesadas (pega o maior peso e as pessoas que tem esse mesmo peso)
# - uma listagem com as pessoas mais leves (pega o menor peso e as pessoas que tem esse mesmo peso)

pessoas = []
dados = []
pesado = leve = cont = 0
nomeP = ''
nomeL = ''

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso [Kg]: ')))
    pessoas.append(dados[:])
    dados.clear()
    cont += 1

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if opcao == 'N':
        break
    else:
        pass

for p in pessoas:
    pesado = leve = pessoas[0][1]
    if p[1] >= pesado:
        pesado = p[1]
        nomeP = p[0]
    if p[1] <= leve:
        leve = p[1]
        nomeL = p[0]

print('=+'*25)
print(f'Foram registradas {cont} pessoas.')
print(f'Quem teve o maior peso foi {nomeP} com {pesado}Kg.')
print(f'Quem teve o menor peso foi {nomeL} com {leve}Kg.')

# outra maneira
'''
temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    princ.append(temp[:])
    temp.clear()

    resp = str(input('Quer continuar [s/n]? '))
    if resp in 'Nn':
        break

print('=+'*30)
print(f'Voce cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi {maior}Kg, com ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi {menor}Kg, com ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
'''