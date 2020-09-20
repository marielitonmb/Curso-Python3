# Aula 16 - Desafio 77: Contando vogais em tupla
# Criar uma tupla com varias palavras (sem acentos).
# Depois mostrar, para cada palavra, as suas vogais.

palavras = ('casa', 'amarelo', 'python', 'oito', 'historia')
vogais = ('a', 'e', 'i', 'o', 'u')
achados = ''

for i in range(0, len(palavras)):
    for v in palavras[i]:
        if v in vogais:
            achados += v
    print(f'A palavra \033[1;4m{palavras[i].upper()}\033[m tem as vogais \033[1;4m{achados.upper()}\033[m.')
    achados = ''

# outra maneira
'''
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
'''