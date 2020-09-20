# Aula 07 - Desafio 12: Calculando descontos
# Ler o preço de um produto e mostrar seu novo preço com 5% de desconto

preco = float(input('Informe o preço do produto: '))

print(f'Voce ganhou 5% de desconto. O novo valor eh \033[33mR${preco - (preco*0.05):.2f}\033[m')
