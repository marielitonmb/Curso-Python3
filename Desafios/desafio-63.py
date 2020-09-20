# Aula 14 - Desafio 63: Sequencia de Fibonacci v1.0
# Ler um numero n inteiro e mostrar os n primeiros elementos da sequencia de Fibonacci.
# Ex: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
# F[n] = F[n-1] + F[n-2]

loop = True
atual = 0
p, s = 1, 1  # primeiro e segundo termos da sequencia
while loop:
    f = int(input('Digite um numero: '))
    print(f'=== Sequencia de Fibonacci ate o {f}º termo ===')
    if f == 1:
        print(f'{p}', end=' ')
    elif f == 2:
        print(f'{p} {s}', end=' ')
    elif f >= 3:
        print(p, s, end=' ')
        for n in range(2, f):
            atual = p + s
            p = s
            s = atual
            print(atual, end=' ')
    else:
        loop = False
    p, s, atual = 1, 1, 0
    loop = False
print('FIM!')

# outra maneira
'''
n = int(input('Digite um numero: '))
t1 = 0
t2 = 1
print('-'*30)
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM!')
'''