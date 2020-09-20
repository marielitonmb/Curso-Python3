# Aula 16 - Desafio 75: Analise de dados em uma tupla
# Ler 4 valores pelo teclado e guarda-los numa tupla, depois mostrar:
# - quantas vezes apareceu o valor 9
# - em que posiçao foi digitado o primeiro valor 3
# - quais foram os numeros pares

tupla = (int(input('Digite um numero: ')), int(input('Digite um numero: ')),
        int(input('Digite um numero: ')), int(input('Digite um numero: ')))

print(tupla)

print(f'O numero 9 apareceu {tupla.count(9)} vez(es).')

if 3 in tupla:
    print(f'O numero 3 apareceu pela primeira vez na posiçao {tupla.index(3)}')
else:
    print(f'O numero 3 nao apareceu na lista')

print('Os numeros pares digitados foram: ', end='')
for p in tupla:
    if p % 2 == 0:
        par = p
        print(par, end=' ')
