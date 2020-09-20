# Aula 19 - Desafio 95: Aprimorando os dicionarios
# Aprimorar o desafio 93 para que ele funcione com varios jogadores.
# incluir um sistema de visualizaçao de detalhes do aproveitamento de cada jogador.
'''
cod nome     gols         total
-------------------------------
0 -----     [3, 2]        5
1 -----     [2, 0, 4]     6
2 -----     [0, 0, 0, 0]  0

Mostrar dados de qual jogador? >> 1  # 999 encerra o loop
-- Detalhamento do jogador: ----
no jogo 0 fez 2 gols
no jogo 1 fez 0 gols
no jogo 2 fez 4 gols
'''

time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    tot = int(input(f'Quantas partidas {jogador["nome"]} disputou? '))
    partidas.clear()
    for i in range(tot):
        partidas.append(int(input(f' - Quantos gols ele fez na {i+1}ª partida? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('+='*20)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    busca = int(input('Mostrar dados de qual jogador (999 p/ parar)? '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Nao existe jogador com codigo {busca}!')
    else:
        print(f'=== DADOS DO JOGADOR: {time[busca]["nome"]} ===')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'  -> no jogo {i+1} fez {g} gols.')
    print('+='*20)
print('FIM!')
