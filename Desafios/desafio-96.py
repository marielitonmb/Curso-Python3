# Aula 20 - Desafio 96: Funçao que calcula area
# Fazer um programa c/ uma funçao chamada area().
# Ela recebe as dimensoes de um terreno retangular (largura e comprimento) e mostra a area do terreno.

def area(larg, comp):
    a = larg * comp
    print(f'A largura {larg}m e o comprimento {comp}m formam uma area de {a}m².')


l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
