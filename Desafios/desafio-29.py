# Aula 10 - Desafio 29: Radar eletronico
# Ler a velocidade de um carro e se ela estiver menor ou igual que 80Km, nada acontece
# Caso contrario, será aplicada uma multa de R$7,00 por Km acima do limite

vel = int(input('Informe a velocidade do carro em Km/h: '))

if vel > 80:
    print('Voce foi multado por estar acima da velociade permitida!')
    print(f'A multa eh de R${(vel-80)*7}')
else:
    print('Muito bem. Mantenha sua velociade abaixo dos 80 Km/h.')
