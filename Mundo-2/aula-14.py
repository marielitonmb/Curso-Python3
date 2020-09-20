# Aula 14 - Estrutura de repetição while

'''
c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')
'''

'''
r = 'S'
while r == 'S':
    n = int(input('Digite um numero: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('FIM')
'''

n = 1
par, impar = 0, 0
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Voce digitou {par} numeros pares e {impar} impares!')
