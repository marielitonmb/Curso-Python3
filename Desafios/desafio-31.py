# Aula 10 - Desafio 31: Custo da viagem
# Pedir a distancia de uma viagem em seguida:
# se a viagem for até 200Km de distancia, o valor da passagem será de R$0,50 por Km rodado
# se for maior que 200 Km, o valor sera de R$0,45 por Km rodado

d = int(input('Informe a distancia em Km da sua viagem: '))

if d <= 200:
    print(f'O preço da passagem eh de R${d*0.5:.2f}')
else:
    print(f'O preço da passagem eh de R${d*0.45:.2f}')

'''
# Outra maneira
preço = d * 0.5 if d <= 200 else d * 0.45
print(f'O preço da passagem eh de R${preço:.2f}')
'''