# Aula 15 - Desafio 66: Varios numeros com flag
# Ler varios numeros inteiros e so parar quando for digitado a flag '999', que eh a condiçao de parada.
# No final mostrar quantos numeros foram digitados e a soma de todos eles (desconsiderando a flag).
cont = soma = 0
while True:
    num = int(input('Digite um numero [999 p/ parar]: '))
    if num == 999:
        break
    else:
        soma += num
        cont += 1
print(f'A soma dos \033[1m{cont}\033[m numeros digitados foi igual a \033[1m{soma}\033[m.')
