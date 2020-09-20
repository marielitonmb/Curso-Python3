# Aula 12 - Desafio 45: JOGO - Pedra, Papel ou Tesoura (Jokenpo)
# Faça o computador jogar jokenpo contra o usuario

import random
import emoji
import time

# site com os codigos dos emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
tesoura = ':v:'
pedra = ':fist:'
papel = ':hand:'

lista = ['PEDRA', 'PAPEL', 'TESOURA']
random.shuffle(lista)

print(emoji.emojize(f'Vamos jogar Pedra {pedra}, Papel {papel} e Tesoura {tesoura}?', use_aliases=True))

print('Pra jogar informe sua opçao:\n'
      '\033[1;4m[1] PEDRA\033[m\n'
      '\033[1;4m[2] PAPEL\033[m\n'
      '\033[1;4m[3] TESOURA\033[m')
jogada = int(input('=> '))

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!')
print('=-='*10)

if jogada == 1:
    print(emoji.emojize(f'Escolha do jogador = PEDRA {pedra}', use_aliases=True))
    print(f'Escolha do computador = {lista[0]}')
    if lista[0] == 'PAPEL':
        print('Voce PERDEU! PAPEL vence a PEDRA')
    elif lista[0] == 'TESOURA':
        print('Parabens, voce VENCEU! PEDRA vence a TESOURA')
    else:
        print('EMPATE!')

elif jogada == 2:
        print(emoji.emojize(f'Escolha do jogador = PAPEL {papel}', use_aliases=True))
        print(f'Escolha do computador = {lista[0]}')
        if lista[0] == 'PEDRA':
            print('Parabens, voce VENCEU! PAPEL vence a PEDRA')
        elif lista[0] == 'TESOURA':
            print('Voce PERDEU! TESOURA vence o PAPEL')
        else:
            print('EMPATE!')

elif jogada == 3:
        print(emoji.emojize(f'Escolha do jogador = TESOURA {tesoura}', use_aliases=True))
        print(f'Escolha do computador = {lista[0]}')
        if lista[0] == 'PEDRA':
            print('Voce PERDEU! PEDRA vence a TESOURA')
        elif lista[0] == 'PAPEL':
            print('Parabens, voce VENCEU! TESOURA vence o PAPEL')
        else:
            print('EMPATE!')
else:
    print('Jogada nao reconhecida!')

print('=-='*10)
