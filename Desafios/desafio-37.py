# Aula 12 - Desafio 37: Conversor de bases numericas
# Leia um numero inteiro e peça pra usuario escolher a base de conversao:
# 1 - p/ binario; 2 - p/ octal; 3 - hexadecimal

num = int(input('Digite um numero: '))
print('Escolha uma das opçoes de conversao abaixo')
print('[ 1 ] Binario | [ 2 ] Octal | [ 3 ] Hexadecimal')
opcao = int(input('Sua opçao: '))

if opcao == 1:
    binario = bin(num)
    print(f'{num} em binario = \033[1;7m{binario[2:]}\033[m')  # o [2:] tira os dois primeiros caracteres '0b'
elif opcao == 2:
    octal = oct(num)
    print(f'{num} em octal = \033[1;7m{octal[2:]}\033[m')  # o [2:] tira os dois primeiros caracteres '0o'
elif opcao == 3:
    hexa = hex(num)
    print(f'{num} em hexadecimal = \033[1;7m{hexa[2:]}\033[m')  # o [2:] tira os dois primeiros caracteres '0x'
else:
    print('Opçao invalida!')
