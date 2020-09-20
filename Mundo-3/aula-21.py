# Aula 21 - Funções (Parte 2)

def fatorial(num=1):
    """
    -> Funçao pra calcular o fatorial de um numero inteiro
    :param num: recebe um numero inteiro maior que zero (num = 1 caso nenhum numero seja informado)
    :return: retona o fatorial do numero informado
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um numero: '))
print(f'O fatorial de {n} eh {fatorial(n)}')
help(fatorial)

# ---------------------------

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um numero: '))
resp = par(num)
if resp:
    print(f'O numero eh par!')
else:
    print(f'O numero eh impar!')
