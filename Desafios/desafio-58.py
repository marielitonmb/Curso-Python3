# Aula 14 - Desafio 58: Jogo da advinhaçao v2.0
# Melhorar o jogo do desafio 28. Dessa vez o jogador ira tentar ate acertar.
# No final deve-se mostrar quantos palpites foram gastos ate acertar.

import random

num_pc = random.randint(1, 10)
palpites = 1
loop = True
print('=== JOGO DA ADVINHAÇAO V2.0 ===')
while loop:
    print('-='*16)
    num = int(input('Digite um numero entre 1 e 10: '))
    print('-='*16)
    if num == num_pc:
        print('\033[1;32mVOCE VENCEU!!!\033[m')
        print(f'O numero que voce digitou \033[1m({num})\033[m foi igual ao sorteado pelo computador.')
        loop = False
    else:
        palpites += 1
        print(f'O seu palpite \033[1m({num})\033[m foi diferente do sorteado pelo computador.')
        if num > num_pc:
            print('Tente novamente! Um pouco mais pra baixo.')
        elif num < num_pc:
            print('Tente novamente! Um pouco mais pra cima.')

if palpites == 1:
    print('UAU! Voce acertou de primeira!')
elif 2 <= palpites <= 5:
    print('Ate que nao precisou arriscar tanto.')
else:
    print('Nossa, voce nao eh bom de palpite mesmo, hein!')
print(f'Ate acertar, voce tentou \033[1m{palpites} vezes\033[m.')
