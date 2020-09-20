# Aula 12 - Desafio 42: Analisando triangulos v2.0
# Refazer o Desafio 35 e informar na resposta se o triangulo formado eh:
# EQUILATERO, com todos os lados iguais
# ISOCELES, com dois lados iguais
# ESCALENO, todos os lados diferentes

a = float(input('Reta 1: '))
b = float(input('Reta 2: '))
c = float(input('Reta 3: '))

if abs(b - c) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a - b) < c < (a + b):
    print('\033[1;4mEH POSSIVEL\033[m formar um triangulo com essas retas!')
    if a == b == c:
        print('E ele eh um triangulo \033[1mEQUILATERO!\033[m')
    elif a != b != c != a:
        print('E ele eh um triangulo \033[1mESCALENO!\033[m')
    else:
        print('E ele eh um triangulo \033[1mISOCELES!\033[m')
else:
    print('\033[1;4mNAO EH POSSIVEL\033[m formar um triangulo com essas retas.')
