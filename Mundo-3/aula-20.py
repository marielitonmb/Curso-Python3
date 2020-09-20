# Aula 20 - Funções (Parte 1)

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


soma(-9, 5)
soma(b=4, a=7)

# ---------------------------

def contador(* num):  # o * desempacota parametros de tamanho desconhecido
    tam = len(num)
    print(f'Recebi os valores {num} que formam um conjunto de {tam} valores.')


contador(2, 6, 4)
contador(7, 5, 1, 9, 4)
contador(4, 2)

# ---------------------------

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [4, 2, 9, 22, 7]
dobra(valores)
print(valores)

# ---------------------------

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(4, 6)
soma(8, 4, -9)
soma(7, -5, 4, -3, 8)
