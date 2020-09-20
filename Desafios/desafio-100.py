# Aula 20 - Desafio 100: Funçoes para sortear e somar
# O programa deve ter uma lista chamada numeros e duas funçoes chamadas sorteia() e somaPar().
# A primeira funçao vai sortear 5 numeros e vai coloca-los dentro da lista.
# A segunda funçao vai mostrar a soma entre todos os valores PARES sorteados pela funçao anterior.

from random import randint

def sorteia(lista):
    for i in range(0, 5):
        lista.append(randint(1, 10))
    print(f'Os valores sorteados foram: {lista}')

def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos valores PARES sorteados deu: {soma}')

numeros = list()
sorteia(numeros)
somaPar(numeros)
