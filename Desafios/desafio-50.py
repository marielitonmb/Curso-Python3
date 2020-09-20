# Aula 13 - Desafio 50: Soma dos pares
# Ler 6 numeros inteiros e mostrar apenas a soma daqueles que forem pares.
# Desconsidere valores impares digitados

soma, pares = 0, 0

for i in range(1, 7):
    num = int(input(f'Digite o {i}º numero: '))
    if num % 2 == 0:
        soma += num
        pares += 1
print(f'A soma dos {pares} valores pares eh \033[7m{soma}\033[m')
