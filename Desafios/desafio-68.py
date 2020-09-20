# Aula 15 - Desafio 68: Jogo do par ou impar
# Programa pra jogar par ou impar com o computador. O jogo eh interrompido quando o jogador perder.
# No final, mostrar o total de vitorias consecutivas do jogador.
from random import randint
num_pc = vitorias = soma = 0

print('\033[7m=== JOGO DO PAR OU IMPAR ===\033[m')
while True:
    num = int(input('Digite um numero: '))
    opcao = str(input('O que vai escolher, PAR ou IMPAR [P/I]: ')).upper().strip()[0]
    if opcao == 'P':
        opcao_pc = 'I'
    elif opcao == 'I':
        opcao_pc = 'P'
    num_pc = randint(0, 10)
    soma = num + num_pc

    if opcao == 'P':
        if soma % 2 == 0:
            print('\033[1;4mVOCE VENCEU!\033[m')
            print(f'Voce colocou \033[1m{num}\033[m e o computador \033[1m{num_pc}\033[m, somados deu \033[1m{soma}\033[m que EH PAR!')
            print()
            vitorias += 1
        else:
            print('\033[1;4mVOCE PERDEU!\033[m')
            print(f'Voce colocou \033[1m{num}\033[m e o computador \033[1m{num_pc}\033[m, somados deu \033[1m{soma}\033[m que EH IMPAR!')
            print()
            break
    elif opcao == 'I':
        if soma % 2 != 0:
            print('\033[1;4mVOCE VENCEU!\033[m')
            print(f'Voce colocou \033[1m{num}\033[m e o computador \033[1m{num_pc}\033[m, somados deu \033[1m{soma}\033[m que EH IMPAR!')
            print()
            vitorias += 1
        else:
            print('\033[1;4mVOCE PERDEU!\033[m')
            print(f'Voce colocou \033[1m{num}\033[m e o computador \033[1m{num_pc}\033[m, somados deu \033[1m{soma}\033[m que EH PAR!')
            print()
            break
print(f'FIM DO JOGO!')
print(f'Voce conseguiu \033[1m{vitorias}\033[m vitoria(s) consecutiva(s).')

# outra maneira
'''
from random import randint
v = 0

while True:
    jogador = int(input('Informe um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [P/I]? ')).strip(.upper())[0]
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total}.', end=''
    print('DEU PAR!' if total % 2 == 0 else 'DEU IMPAR!')

    if tipo == 'P':
        if total % 2 == 0:
            print('VOCE VENCEU!')
            v += 1
        else:
            print('VOCE PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCE VENCEU!')
            v += 1
        else:
            print('VOCE PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voce venceu {v} vezes.')
'''