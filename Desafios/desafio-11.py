# Aula 07 - Desafio 11: Pintando parede
# Ler os valores da altura e largura de uma parede e calcular a quantidade de tinta pra pintar

altura = int(input('Informe a altura da parede: '))
largura = int(input('Informe a largura da parede: '))

area = altura * largura
tinta = area / 2

print(f'A parede tem \033[33m{area}m²\033[m de area e sera necessario \033[36m{tinta}l\033[m de tinta para pinta-la')
