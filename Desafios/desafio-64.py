# Aula 14 - Desafio 64: Tratando varios valores v1.0
# Ler varios numeros inteiros. O programa so para quando o usuario digitar '999', que e o flag de parada.
# No final, mostrar quantos numeros foram digitados e a soma entre eles (sem contar a flag).

soma, cont = 0, 0
loop = True
while loop:
    num = int(input('Digite um numero [p/ parar digite 999]: '))
    if num == 999:
        loop = False
    else:
        soma += num
        cont += 1
print(f'A soma dos \033[1;32m{cont}\033[m numeros digitados foi \033[1;32m{soma}\033[m.')

# outra maneira
'''
num = cont = soma = 0
num = int(input('Digite um numero [p/ parar digite 999]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero [p/ parar digite 999]: '))
print(f'Voce digitou {cont} numeros e a soma foi igual a {soma}.')
'''