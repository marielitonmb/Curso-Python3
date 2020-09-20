# Aula 13 - Estrutura de repetição for

for c in range(5, 0, -1):
    print(c)

print('-=' * 10)

for i in range(1, 6, 2):
    print(i)

print('-=' * 10)

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print('FIM')
