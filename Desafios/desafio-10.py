# Aula 07 - Desafio 10: Conversor de moedas
# Informar a cotação do dolar atual

real = float(input('Digite o valor em Reais: '))

dolar = real / 5.35  # cotaçao em 06/05/2020

print(f'R$ {real} equivale a US$ {dolar:.2f}')
