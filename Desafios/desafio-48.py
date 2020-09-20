# Aula 13 - Desafio 48: Soma impares multiplos de tres
# Calcular a soma entre todos os numeros impares multiplos de 3 dentro do intervalo de 1 a 500

soma, cont = 0, 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        soma += num
        cont += 1
print(f'A soma entre os \033[4m{cont}\033[m valores multiplos de 3 entre 1 e 500 eh igual a \033[7m{soma}\033[m')
