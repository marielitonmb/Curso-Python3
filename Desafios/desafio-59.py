# Aula 14 - Desafio 59: Criando um menu de opçoes
# Ler dois valores e mostrar um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos numeros
# [5] sair do programa
# O programa deve fazer cada operaçao solicitada no menu.

maior = []
loop, fim = True, True
while fim:
    print('\033[7m==== Digite dois numeros ====\033[m')
    n1 = int(input('1º numero: '))
    n2 = int(input('2º numero: '))
    loop = True
    while loop:
        print('\033[7m=+=+= Menu de Opçoes =+=+=\033[m')
        print('[1] Somar os dois numeros\n'
              '[2] Multiplicar os dois numeros\n'
              '[3] Informar o maior numero\n'
              '[4] Informar novos numeros\n'
              '[5] Sair do programa')
        opcao = int(input('>> '))

        if opcao == 1:
            soma = n1 + n2
            print(f'\033[1;32m{n1} + {n2} = {soma}\033[m')
        elif opcao == 2:
            mult = n1 * n2
            print(f'\033[1;32m{n1} * {n2} = {mult}\033[m')
        elif opcao == 3:
            if n1 == n2:
                print('\033[1;32mAmbos os numeros sao iguais.\033[m')
            else:
                maior = n1, n2
                print(f'\033[1;32m{max(maior)} eh o maior numero.\033[m')
        elif opcao == 4:
            loop = False
        elif opcao == 5:
            loop = False
            fim = False
        else:
            print('Opçao Invalida!')

print('\033[1;4mFIM DO PROGRAMA!\033[4m')
