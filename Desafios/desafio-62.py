# Aula 14 - Desafio 62: Super progressao aritmetica v3.0
# Melhorar o desafio 61. Perguntar ao usuario se ele quer mostrar mais alguns termos do PA.
# O programa encerra quando ele disser que quer mostrar '0 termos'.

opcao, loop = True, True
while loop:
    if opcao:
        primeiro = int(input('Informe o primeiro valor da PA: '))
        razao = int(input('Informe a razao da PA: '))
        decimo = primeiro + (10 - 1) * razao

        print('PA = ', end='')
        for c in range(primeiro, decimo + razao, razao):
            print(f'{c} -> ', end='')
        print('\n')
        continua = input('Quer ver mais algum termo dessa PA [S/N]? ').strip().lower()

        if continua == 's':
            n = int(input('Informe quantos termos deseja: '))
            if n == 0:
                print()
                opcao = False
            else:
                decimo = primeiro + ((10 + n) - 1) * razao
                print('PA = ', end='')
                for c in range(primeiro, decimo + razao, razao):
                    print(f'{c} -> ', end='')
                print('\n')
        else:
            print()
            opcao = True
    else:
        loop = False
print('FIM!')

# outra maneira
'''
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais quer mostrar? '))
print('FIM!')
print(f'PA concluida com {termo} termos mostrados.')
'''