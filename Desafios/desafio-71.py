# Aula 15 - Desafio 71: Simulador de caixa eletronico
# Simular o funcionamento de uma caixa eletronico. No inicio, pergunte ao usuario o valor (int) a ser sacado.
# O programa deve informar quantas cedulas de cada valor serao entregues.
# Obs: as cedulas sao R$50, R$20, R$10 e R$1
c50 = c20 = c10 = c1 = resto1 = resto2 = 0
valor = int(input('Informe quanto deseja sacar R$: '))
while True:
    c50 = valor // 50
    resto1 = valor % 50
    c20 = resto1 // 20
    resto2 = resto1 % 20
    c10 = resto2 // 10
    c1 = valor % 10
    break
print('==== LIBERANDO QUANTIA ====')
print(f'{c50} cedula(s) de R$ 50,00')
print(f'{c20} cedula(s) de R$ 20,00')
print(f'{c10} cedula(s) de R$ 10,00')
print(f'{c1} cedula(s) de R$ 1,00')

# outra maneira
'''
valor = int(input('Quanto deseja sacar? R$: '))
total = valor
ced = 50
total_ced = 0
while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} cedulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break
'''