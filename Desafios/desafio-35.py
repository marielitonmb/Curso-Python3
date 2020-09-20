# Aula 10 - Desafio 35: Analisando triangulo v1.0
# Leia o valor de 3 retas e dizer se podem ou não formar um triângulo

a = float(input('Reta 1: '))
b = float(input('Reta 2: '))
c = float(input('Reta 3: '))

if abs(b - c) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a - b) < c < (a + b):
    print('\033[1;4mEH POSSIVEL\033[m formar um triangulo com essas retas!')
else:
    print('\033[1;4mNAO EH POSSIVEL\033[m formar um triangulo com essas retas.')
