# Aula 13 - Desafio 55: Maior e menor da sequencia
# Ler o peso de 5 pessoas, no final mostrar qual foi o maior e menor peso lido

peso = []

for i in range(1, 6):
    peso.append(float(input(f'Peso {i}: ')))

print(f'O maior peso eh \033[1m{max(peso)}Kg\033[m e o menor eh \033[1m{min(peso)}Kg\033[m')

'''
### outro jeito ###

maior, menor = 0, 0

for p in range(1, 6):
    peso = float(input(f'Peso {p}: '))
    if p == 1:
        menor, maior = peso, peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso foi {maior}Kg e o menor foi {menor}Kg')
'''