# Aula 19 - Desafio 93: Cadastro de jogador de futebol
# Ler o nome do jogador e quantas partidas ele jogou. Depois ler a quantidade de gols em cada partida
# (colocar a quantidade de gols numa lista).
# No final, tudo isso sera guardado num dicionario incluindo o total de gols feitos durante o campeonato.

cadastro = dict()
gols = list()

jogador = str(input('Nome do jogador: ')).strip().capitalize()
partidas = int(input(f'Quantas partidas {jogador} disputou? '))
for i in range(partidas):
    gols.append(int(input(f'Quantos gols ele fez na {i+1}ª partida? ')))

cadastro['jogador'] = jogador
cadastro['partidas'] = partidas
cadastro['gols'] = gols
cadastro['total de gols'] = sum(gols)

print('=+'*20)
print(cadastro)

print('=+'*20)
for k, v in cadastro.items():
    print(f'O campo {k} tem o valor {v}.')

print('=+'*20)
print(f'O jogador {cadastro["jogador"]} disputou {len(cadastro["gols"])} partidas.')
for i, v in enumerate(cadastro['gols']):
    print(f' => Na partida {i+1}, fez {v} gols.')
print(f'{cadastro["jogador"]} fez um total de {cadastro["total de gols"]} gols.')
