# Aula 21 - Desafio 102: Funçao para fatorial
# Criar uma funçao chamada fatorial() que receba dois paramentros.
# O primeiro indica o numero a ser calculado e o outro chamado 'show',
# sera o valor logico (opcional) indicando se sera mostrado ou nao
# na tela o processo de calculo do fatorial.
# Obs: adicionar um docstring p/ funçao

def fatorial(num=1, show=False):
    """
    -> Funçao que calcula o fatorial de um numero.
    :param num: numero que sera calculado o fatorial.
    :param show: (Opcional) mostrar ou nao na tela o calculo do fatorial
    :return: -
    """
    from math import factorial
    if show:
        c = num
        f = 1
        print(f'{num}! = ', end='')
        while c > 0:
            print(f'{c} ', end='')
            print('x ' if c > 1 else '= ', end='')
            f *= c
            c -= 1
        print(f)
    else:
        print(f'{num}! = ', end='')
        print(factorial(num))


fatorial(8, show=True)
help(fatorial)

# outra maneira
'''
def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(fatorial(6, True))
'''