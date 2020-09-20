# Aula 8 - Desafio 17: Catetos e hipotenusa
# Ler o comprimento do cateto oposto e do catedo adjacente e calcular a hipotenusa

from math import hypot

cat_op = float(input('Cateto oposto: '))
cat_ad = float(input('Cateto adjacente: '))

print(f'O valor da hipotenusa eh \033[1;37;40m{hypot(cat_op, cat_ad):.2f}\033[m')
