# Aula 10 - Desafio 34: Aumentos multiplos
# Leia o salario de um funiconario e calcular o aumento:
# salarios acima de R$1250 o aumento é de 10%
# salarios abaixo ou iguais o aumento é de 15%

salario = float(input('Informe seu salario: '))

if salario > 1250:
    aumento = salario + (salario*0.1)
else:
    aumento = salario + (salario*0.15)

print(f'Seu novo salario eh de R${aumento:.2f}')
