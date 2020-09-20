# Aula 21 - Desafio 103: Ficha do jogador
# Criar uma funçao chamada ficha(), que receba dois parametros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa deve mostrar a ficha do jogador, mesmo que algum dado nao tenha
# sido informado corretamente.

def ficha(j, g):
    if j == '':
        j = '<desconhecido>'
    if g == '' or g.isnumeric() == False:
        g = 0
    print(f'O jogador {j} fez {g} gol(s) no campeonato.')


jogador = str(input('Nome do jogador: ')).strip().capitalize()
gols = str(input('Quantos gols ele marcou? '))
ficha(jogador, gols)

# outra maneira
'''
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do jogador: '))
g = str(input('Numero de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
'''