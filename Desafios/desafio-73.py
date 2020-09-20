# Aula 16 - Desafio 73: Tuplas com times de futebol
# Criar uma tupla com os 20 clubes do Brasileirao na ordem de colocaçao. Depois mostrar:
# - Apenas os 5 primeiros colocados
# - Os ultimos 4 colocados
# - Uma lista com os times em ordem alfabetica
# - Em que posiçao da tabela esta o time do Flamengo

# Tabela do Brasileirao 2020 (Covidao) em 20/08/2020

times = ('Internacional', 'Atletico-MG', 'Vasco da Gama', 'Bahia', 'Athletico-PR', 'Gremio', 'Botafogo',
          'Palmeiras', 'RB Bragantino', 'Corinthians', 'Santos', 'Atletico-GO', 'Fluminense', 'Sport Recife',
          'Fortaleza', 'Flamengo', 'Sao Paulo', 'Ceara SC', 'Goias', 'Coritiba')

print('\033[7mTimes do Brasileirao 2020:\033[m')
print(times)
print()
print('\033[7mA zona da Libertadores eh formada por:\033[m')
for l in range(0, 5):
    print(f'{l+1}º {times[l]}', end=', ')  # poderia fazer sem o FOR usando print(f'{times[0:5]}')
print('\n')
print('\033[7mA zona de rebaixamento eh formada por:\033[m')
for z in range(0, 4):
    print(f'{17+z}º {times[-4+z]}', end=', ')  # poderia fazer sem o FOR usando print(f'{times[-4:]}')
print('\n')
print('\033[7mTimes em ordem alfabetica:\033[m')
print(sorted(times))
print()
print(f'\033[7mO Flamengo (atualmente) esta na {times.index("Flamengo")+1}ª posiçao.\033[m')
