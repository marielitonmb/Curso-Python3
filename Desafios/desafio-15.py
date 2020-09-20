# Aula 07 - Desafio 15: Aluguel de carros
# Ler os Km rodados por um carro alugado e quantos dias ficou alugado e calcular o valor a ser pago
# O valor do aluguel por dia é R$60,00 e o valor por KM rodado é R$0,15

d = int(input('Informe a quantidade de dias em que o carro ficou alugado: '))
km = int(input('Informe quanto Km foram percorridos nesse periodo: '))

p = d * 60 + km * 0.15

print(f'O valor a ser pago pelo aluguel no periodo de {d} dias com {km}km rodados eh de R${p:.2f}')
