# Aula 15 - Desafio 70: Estatisticas em produtos
# Ler o nome e o preço de varios produtos. O programa deve perguntar se o usuario vai continuar.
# No final, mostre:
# - qual o total gasto
# - quantos produtos custam mais de R$1000
# - qual eh o nome do produto mais barato
total = contMil = menor = 0
barato = ''
while True:
    produto = str(input('Informe o produto: ')).strip()
    preco = float(input('Informe o preço R$: '))

    if total == 0 or preco < menor:
        menor = preco
        barato = produto
    if preco >= 1000:
        contMil += 1
    total += preco

    opcao = ' '
    while opcao not in 'sn':
        opcao = str(input('Deseja continuar [S/N]: ')).lower().strip()[0]
    if opcao == 'n':
        break
    elif opcao == 's':
        pass

print('======== FECHAMENTO DOS PEDIDOS ========')
print(f'Valor total dos produtos R$ {total:.2f}')
print(f'{contMil} produtos estao acima dos R$ 1000,00')
print(f'O produto mais barato foi {barato}, custando R$ {menor:.2f}')
