# Aula 18 - Desafio 88: palpites para a Mega-Sena
# O programa ira perguntar ao usuario quantos jogos serao gerados e vai sortear 6 numeros entre 1 e 60 (sem repetiçoes!)
# para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

jogo = []
sorteio = []

opcao = int(input('Quantos jogos deseja fazer? '))

for i in range(opcao):
    for n in range(0, 6):
        num = randint(1, 60)
        if num not in sorteio:  # Evita que entre numero repetido na lista
            sorteio.append(num)
        else:
            pass
    sorteio.sort()  # Deixa os numeros em ordem crescente
    jogo.append(sorteio[:])
    sorteio.clear()

print('Os jogos gerados foram:')
for c in range(opcao):
    print(jogo[c])  # Lista cada jogo um abaixo do outro

# outra maneira
'''
from random import randint
from time import sleep
lista = []
jogos = []
print('='*30)
print('    JOGA NA MEGA SENA      ')
print('='*30)
quant = int(input('Quantos jogos quer fazer? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('=+'*3, f' SORTEANDO {quant} JOGOS ', '=+'*3)
sleep(1)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('*-'*3, '<< BOA SORTE! >>', '*-'*3)
'''