# Aula 15 - Interrompendo repetições while

cont = soma = 0
while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    soma += num
    cont += 1
print('FIM!')
print(f'Os {cont} numeros somados deram = {soma}.')
