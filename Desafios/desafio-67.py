# Aula 15 - Desafio 67: Tabuada v3.0
# Mostrar a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario.
# O programa para quando o valor digitado for negativo.
while True:
    n = int(input('Digite um numero: '))
    if n < 0:
        break
    else:
        opcao = int(input('Escolha uma operaçao:\n'
                          '[1] ADIÇAO\n'
                          '[2] SUBTRAÇAO\n'
                          '[3] MULTIPLICAÇAO\n'
                          '[4] DIVISAO\n'
                          '>> '))
        if opcao == 1:
            print(f'\033[4mTabuada de adiçao\033[m')
            for num in range(1, 11):
                print(f'{n} + {num:2} = {n+num:2}')
            print()
        elif opcao == 2:
            print(f'\033[4mTabuada de subtraçao\033[m')
            for num in range(1, 11):
                print(f'{n} - {num:2} = {n-num:2}')
            print()
        elif opcao == 3:
            print(f'\033[4mTabuada de multiplicaçao\033[m')
            for num in range(1, 11):
                print(f'{n} * {num:2} = {n*num:2}')
            print()
        elif opcao == 4:
            print(f'\033[4mTabuada de divisao\033[m')
            for num in range(1, 11):
                print(f'{n} / {num:2} = {n/num:.2f}')
            print()
        else:
            print('Opçao Invalida!')

print('FIM!')
